# Session 3 Learning Guide: Dataset and Evaluator Setup

## Goal

Prepare a valid JSONL evaluation dataset and define evaluator configuration aligned with Session 1 targets.

## Inputs You Will Use

- Session brief in `Session3/Session3.md`
- Solution notebook `solutions/Session3/session3_dataset_and_evaluators.ipynb`
- Sample data `solutions/data/session3_test_queries.jsonl`
- Dataset upload helper `solutions/src/hackathon_solutions/evaluation_runner.py`

## Step-by-Step

1. Inspect the sample dataset structure.
- Open `solutions/data/session3_test_queries.jsonl`.
- Confirm each line is valid JSON and includes at least:
  - `query`
  - `ground_truth`

2. Run Session 3 notebook Cell 2.
- This resolves the dataset path and loads rows.
- It prints dataset path and row count.
- It parses the first row with `json.loads(...)` as a schema sanity check.

3. Run Session 3 notebook Cell 3.
- Review the evaluator plan:
  - `coherence` (quality)
  - `relevance` (quality)
  - `task_adherence` (agent behavior)
  - `violence` (safety)

4. Validate evaluator dependencies.
- AI-assisted evaluators require a deployed model (`MODEL_DEPLOYMENT_NAME`).
- Relevance and similarity-style checks depend on meaningful `ground_truth` values.

5. Upload your dataset to Foundry (optional in notebook, required in real flow).

```python
from hackathon_solutions.evaluation_runner import upload_dataset
upload_dataset("solutions/data/session3_test_queries.jsonl")
```

6. Record dataset metadata.
- Keep `dataset_name`, `dataset_version`, and returned `dataset_id` for auditability.

## Checkpoint

You are done when:

- Dataset file is valid JSONL.
- Required fields are present in all rows.
- Evaluator configuration is decided and documented.

## Expected Row Example

```json
{"query": "What is Azure AI Foundry?", "ground_truth": "Azure AI Foundry is a platform for building, evaluating, and operating AI applications and agents."}
```

## Troubleshooting

- JSON parse errors: validate one object per line and remove trailing commas.
- Missing `ground_truth`: add references before running relevance-based checks.
- Upload errors: verify project permissions and endpoint configuration.
