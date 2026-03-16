# Session 3 Facilitator Guide: Dataset and Evaluator Setup

## Session Outcome

Participants prepare a valid JSONL test set and align evaluator choices to their risk and quality goals.

## Suggested Duration

- 40 minutes

## Talking Points

1. Dataset quality drives evaluation quality.
- Weak or narrow examples create misleading scores.

2. Keep dataset schema explicit.
- `query` and `ground_truth` are required for this flow.

3. Evaluator choice should be intentional.
- Distinguish behavior, quality, and safety measures.

4. AI-assisted evaluators need model judge configuration.
- Reinforce `MODEL_DEPLOYMENT_NAME` requirement.

## Facilitation Flow

1. Review sample JSONL structure with participants.
2. Run notebook cells to inspect row count and parse sample rows.
3. Review evaluator configuration dictionary.
4. Optionally demonstrate dataset upload to Foundry.

## Questions To Ask Participants

- What user behaviors are missing from your current test set?
- Which evaluator would best detect your current agent weakness?
- Do all rows include fields required by selected evaluators?

## Common Misunderstandings

- Including invalid JSON or multiple objects on one line.
- Using relevance-like metrics without dependable `ground_truth`.

## Session Checkpoint

Each team has:

- A validated JSONL dataset.
- A documented evaluator set and rationale.
