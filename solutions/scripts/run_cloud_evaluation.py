import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = REPO_ROOT / "solutions" / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from hackathon_solutions.config import load_config, validate_config
from hackathon_solutions.foundry_helpers import create_openai_client, load_jsonl


def get_threshold(metric_name: str, default: float) -> float:
    value = os.getenv(metric_name)
    if not value:
        return default
    return float(value)


def build_item_schema(dataset_rows: list[dict]) -> dict:
    properties: dict[str, dict] = {}
    required: list[str] = []

    if not dataset_rows:
        return {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
            "additionalProperties": True,
        }

    keys = set()
    for row in dataset_rows:
        keys.update(row.keys())

    for key in sorted(keys):
        properties[key] = {"type": "string"}

    if "query" in properties:
        required.append("query")

    return {
        "type": "object",
        "properties": properties,
        "required": required,
        "additionalProperties": True,
    }


def build_testing_criteria(model_deployment_name: str, relevance_threshold: float, coherence_threshold: float) -> list[dict]:
    return [
        {
            # "model": model_deployment_name,
            # "range": [0.0, 1.0],
            # "pass_threshold": coherence_threshold,
            "type": "azure_ai_evaluator",
            "name": "coherence",
            "evaluator_name": "builtin.coherence",
            "initialization_parameters": {
                "deployment_name": model_deployment_name,
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{item.ground_truth}}",
            },
        },
        # {
        #     "type": "text_similarity",
        #     "name": "relevance",
        #     "evaluation_metric": "cosine",
        #     "input": "{{sample.output_text}}",
        #     "reference": "{{item.ground_truth}}",
        #     "pass_threshold": relevance_threshold,
        # },
    ]


def run_eval(openai_client, model_deployment_name: str, dataset_rows: list[dict], coherence_threshold: float, relevance_threshold: float):
    eval_name = f"hackathon-eval-{int(time.time())}"

    evaluation = openai_client.evals.create(
        name=eval_name,
        data_source_config={
            "type": "custom",
            "item_schema": build_item_schema(dataset_rows),
            "include_sample_schema": True,
        },
        testing_criteria=build_testing_criteria(
            model_deployment_name=model_deployment_name,
            relevance_threshold=relevance_threshold,
            coherence_threshold=coherence_threshold,
        ),
    )

    run = openai_client.evals.runs.create(
        eval_id=evaluation.id,
        name=f"{eval_name}-run",
        data_source={
            "type": "responses",
            "model": model_deployment_name,
            "source": {
                "type": "file_content",
                "content": [{"item": row} for row in dataset_rows],
            },
            "input_messages": {
                "type": "template",
                "template": [{"role": "user", "content": "{{item.query}}"}],
            },
            "sampling_params": {"temperature": 0.0},
        },
    )

    status = str(run.status).lower()
    while status in {"queued", "in_progress"}:
        time.sleep(8)
        run = openai_client.evals.runs.retrieve(run_id=run.id, eval_id=evaluation.id)
        status = str(run.status).lower()

    return evaluation, run


def to_summary(evaluation, run) -> dict:
    criteria: dict[str, dict] = {}
    for result in getattr(run, "per_testing_criteria_results", []):
        passed = int(getattr(result, "passed", 0) or 0)
        failed = int(getattr(result, "failed", 0) or 0)
        total = passed + failed
        pass_rate = (passed / total) if total else 0.0
        name = str(getattr(result, "testing_criteria", "unknown"))
        criteria[name] = {
            "passed": passed,
            "failed": failed,
            "pass_rate": pass_rate,
        }

    result_counts = getattr(run, "result_counts", None)
    counts = {
        "total": int(getattr(result_counts, "total", 0) or 0),
        "passed": int(getattr(result_counts, "passed", 0) or 0),
        "failed": int(getattr(result_counts, "failed", 0) or 0),
        "errored": int(getattr(result_counts, "errored", 0) or 0),
    }

    return {
        "eval_id": evaluation.id,
        "run_id": run.id,
        "run_status": run.status,
        "report_url": getattr(run, "report_url", None),
        "result_counts": counts,
        "criteria": criteria,
    }


def main() -> int:
    load_dotenv()
    cfg = load_config()
    validate_config(cfg)

    coherence_threshold = get_threshold("MIN_COHERENCE", 0.85)
    relevance_threshold = get_threshold("MIN_RELEVANCE", 0.85)

    data_file = Path("solutions/data/session3_test_queries.jsonl")
    if not data_file.exists():
        data_file = Path("data/session3_test_queries.jsonl")

    if not data_file.exists():
        raise FileNotFoundError("Could not find session3_test_queries.jsonl in expected locations")

    dataset_rows = load_jsonl(data_file)
    if not dataset_rows:
        raise ValueError("Dataset is empty. Add at least one JSONL row with a 'query' field")

    if any("query" not in row for row in dataset_rows):
        raise ValueError("Each dataset row must include a 'query' field")

    if any("ground_truth" not in row for row in dataset_rows):
        raise ValueError("Each dataset row must include 'ground_truth' for relevance scoring")

    openai_client = create_openai_client(cfg)
    evaluation, run = run_eval(
        openai_client=openai_client,
        model_deployment_name=cfg.model_deployment_name,
        dataset_rows=dataset_rows,
        coherence_threshold=coherence_threshold,
        relevance_threshold=relevance_threshold,
    )
    summary = to_summary(evaluation, run)

    artifacts = Path("solutions/artifacts")
    artifacts.mkdir(parents=True, exist_ok=True)
    out_file = artifacts / "latest_summary.json"
    out_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("Evaluation summary:")
    print(json.dumps(summary, indent=2))
    print(f"Saved summary to {out_file}")

    if str(summary.get("run_status", "")).lower() != "completed":
        print(f"FAIL: evaluation run did not complete successfully: {summary.get('run_status')}", file=sys.stderr)
        return 1

    coherence = summary.get("criteria", {}).get("coherence", {}).get("pass_rate", 0.0)
    if coherence < coherence_threshold:
        print(
            f"FAIL: coherence pass_rate {coherence} < threshold {coherence_threshold}",
            file=sys.stderr,
        )
        return 1

    relevance = summary.get("criteria", {}).get("relevance", {}).get("pass_rate", 0.0)
    if relevance < relevance_threshold:
        print(
            f"FAIL: relevance pass_rate {relevance} < threshold {relevance_threshold}",
            file=sys.stderr,
        )
        return 1

    print("PASS: quality gates satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
