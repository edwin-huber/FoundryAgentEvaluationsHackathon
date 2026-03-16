# Session 4 Learning Guide: Execute a Cloud Evaluation Run

## Goal

Create an evaluation definition, start a cloud run, poll to completion, and review result signals.

## Inputs You Will Use

- Session brief in `Session4/Session4.md`
- Solution notebook `solutions/Session4/session4_run_cloud_evaluation.ipynb`
- Script reference `solutions/scripts/run_cloud_evaluation.py`

## Step-by-Step

1. Initialize config and OpenAI client.
- Run Session 4 notebook Cell 2.
- This loads env config, validates it, and creates `openai_client` via `get_openai_client()`.

2. Load and validate dataset rows.
- Run Session 4 notebook Cell 3.
- It checks that every row includes `query` and `ground_truth`.
- It constructs `item_schema` from discovered dataset keys.

3. Create evaluation definition.
- In the same cell, call:
  - `openai_client.evals.create(...)`
- Include:
  - `data_source_config` with custom `item_schema`
  - `testing_criteria` with evaluator config (example uses `builtin.coherence`)

4. Launch evaluation run.
- Run Session 4 notebook Cell 5.
- It calls `openai_client.evals.runs.create(...)` with:
  - source rows from the JSONL content
  - input message template using `{{item.query}}`
  - deterministic sampling (`temperature: 0.0`)

5. Poll run status until terminal state.
- Keep retrieving with `openai_client.evals.runs.retrieve(...)`.
- Stop when status is no longer `queued` or `in_progress`.

6. Capture result summary.
- Record:
  - `run_id`
  - `status`
  - `report_url`
  - `result_counts`

## Checkpoint

You are done when run status is `completed` and a report URL is available.

## Optional CLI Equivalent

```bash
python solutions/scripts/run_cloud_evaluation.py
```

This script performs validation, run creation, status polling, summary export, and threshold checks.

## Troubleshooting

- `Rows missing required fields`: normalize your dataset keys.
- Run stuck in progress: verify evaluator config and model deployment availability.
- Non-completed status: inspect run details in Foundry portal via `report_url`.
