# Session 6 Learning Guide: Interpret Results and Apply Quality Gates

## Goal

Interpret evaluation summaries, apply threshold logic, and define sustainable CI evaluation practices.

## Inputs You Will Use

- Session brief in `Session6/Session6.md`
- Solution notebook `solutions/Session6/session6_results_and_quality_gates.ipynb`
- Sample summary `solutions/artifacts/session6_sample_summary.json`
- Latest run summary `solutions/artifacts/latest_summary.json` (from Session 5)

## Step-by-Step

1. Load summary data.
- Run Session 6 notebook Cell 2.
- Start with `session6_sample_summary.json` if no fresh run exists.

2. Define quality thresholds.
- Run Session 6 notebook Cell 3.
- Default thresholds:
  - `coherence: 0.85`
  - `relevance: 0.85`
  - `task_adherence: 0.85`

3. Evaluate pass/fail.
- Use `all(summary.get(metric, 0) >= target ...)` to compute gate status.
- Record final boolean as your deployment gate decision.

4. Investigate weak metrics.
- For any failed threshold, review examples in Foundry evaluation report.
- Identify whether issues come from prompts, tool routing, or missing context.

5. Decide CI policy.
- Choose when to run evaluations:
  - per merge to `main`
  - nightly full suites
  - pre-release extended suites

6. Feed improvements back into earlier sessions.
- Update dataset coverage (Session 3).
- Adjust evaluator mix and thresholds (Session 1).
- Re-run cloud and CI evaluation (Sessions 4 and 5).

## Checkpoint

You are done when:

- You can explain why the gate passed or failed.
- You have a concrete plan to improve at least one weak metric.
- CI trigger strategy is documented for your team.

## Sample Gate Logic

```python
thresholds = {"coherence": 0.85, "relevance": 0.85, "task_adherence": 0.85}
quality_gate = all(summary.get(metric, 0) >= target for metric, target in thresholds.items())
```

## Troubleshooting

- Missing metrics in summary: default to `0` and treat as fail until fixed.
- Inconsistent score trends: run a larger, stable dataset and compare across runs.
- High variance: lower temperature and keep prompts/input format deterministic.
