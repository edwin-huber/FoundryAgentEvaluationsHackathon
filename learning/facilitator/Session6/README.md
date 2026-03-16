# Session 6 Facilitator Guide: Results Interpretation and Quality Gates

## Session Outcome

Participants can explain evaluation outcomes, apply gate logic, and define a practical long-term evaluation cadence.

## Suggested Duration

- 35 minutes

## Talking Points

1. Scores are decision inputs, not the final decision.
- Pair metric values with qualitative examples from reports.

2. Quality gates should be stable and explainable.
- Use simple thresholds first, then evolve with historical data.

3. Evaluation cadence should balance speed and cost.
- Fast checks on merges, broader suites nightly or pre-release.

4. Continuous improvement loop.
- Failures should feed back into dataset and prompt/tool updates.

## Facilitation Flow

1. Load sample or latest summary in notebook.
2. Run gate logic cell and discuss pass/fail result.
3. Ask each team to identify one weak metric and remediation idea.
4. Capture a team-level CI policy for run frequency and blockers.

## Questions To Ask Participants

- Which metric should block deployment immediately?
- Which metric can be monitored before becoming a hard gate?
- What change will you make first to improve your weakest score?

## Common Misunderstandings

- Treating missing metrics as neutral instead of failure risk.
- Updating thresholds too quickly without enough run history.

## Session Checkpoint

Each team submits:

- A pass/fail gate decision with rationale.
- One prioritized improvement action.
- A proposed CI evaluation schedule.
