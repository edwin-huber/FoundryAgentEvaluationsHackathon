# Session 5 Learning Guide: Integrate Evaluation with GitLab CI

## Goal

Automate the cloud evaluation run in GitLab CI so quality checks run on every selected pipeline trigger.

## Inputs You Will Use

- Session brief in `Session5/Session5.md`
- Solution notebook `solutions/Session5/session5_gitlab_ci_integration.ipynb`
- CI template `solutions/templates/gitlab-ci.yml`
- Evaluation script `solutions/scripts/run_cloud_evaluation.py`

## Step-by-Step

1. Review the pipeline template.
- Run Session 5 notebook Cell 2 to print `gitlab-ci.yml`.
- Confirm stages and script sequence:
  - create venv
  - install requirements
  - run cloud evaluation script

2. Copy template to repository root.

```bash
cp solutions/templates/gitlab-ci.yml .gitlab-ci.yml
```

3. Configure GitLab CI/CD variables.
- Required:
  - `PROJECT_ENDPOINT`
  - `MODEL_DEPLOYMENT_NAME`
  - `AZURE_TENANT_ID`
  - `AZURE_CLIENT_ID`
  - `AZURE_CLIENT_SECRET`
- Optional thresholds:
  - `MIN_COHERENCE` (default `0.85`)
  - `MIN_RELEVANCE` (default `0.85`)

4. Review quality gate behavior in the script.
- `run_cloud_evaluation.py` fails the job when:
  - run status is not completed
  - coherence pass rate is below threshold
  - relevance pass rate is below threshold

5. Commit and push to trigger pipeline.
- Check the `evaluate_agent` job logs.
- Confirm it reaches `PASS: quality gates satisfied` for successful runs.

6. Persist artifacts if needed.
- Script writes summary JSON to `solutions/artifacts/latest_summary.json`.
- Store it as a pipeline artifact for traceability.

## Checkpoint

You are done when GitLab pipeline runs and produces a pass/fail outcome based on evaluation thresholds.

## Troubleshooting

- Auth errors in CI: verify service principal values and variable scope/protection.
- Missing dataset file: ensure repository includes `solutions/data/session3_test_queries.jsonl`.
- Unexpected quality-gate failures: inspect `criteria` pass rates in summary output.
