# Session 1 Facilitator Guide: Concepts and Evaluation Plan

## Session Outcome

Participants leave with a baseline evaluator plan and threshold targets to carry into implementation.

## Suggested Duration

- 30 minutes

## Talking Points

1. Agentic evaluation is not only final answer quality.
- Emphasize intent handling, tool routing, and task completion behavior.

2. Three metric categories should always be visible.
- Agent behavior: task adherence, intent resolution, tool call accuracy.
- Quality: coherence, relevance.
- Safety: violence, hate.

3. Thresholds are operational decisions.
- `0.85` is a practical baseline for early quality gates.

4. Metrics must map to product risk.
- Ask teams what failure mode matters most in their scenario.

## Facilitation Flow

1. Open participant guide and notebook for Session 1.
2. Have teams run the evaluation plan cell.
3. Ask each team to choose mandatory vs informational metrics.
4. Ask each team to record deployment-blocking thresholds.

## Questions To Ask Participants

- Which metric best detects your highest-risk failure?
- Which metric would you monitor first during regression?
- Which threshold is strict enough to protect users?

## Common Misunderstandings

- Treating safety metrics as optional by default.
- Setting thresholds without a baseline run.

## Session Checkpoint

Each team can state:

- Their metric set by category.
- Their top three deployment gates.
