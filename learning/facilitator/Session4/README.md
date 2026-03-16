# Session 4 Facilitator Guide: Execute a Cloud Evaluation Run

## Session Outcome

Participants can create and execute a cloud evaluation run and interpret top-level run status and counts.

## Suggested Duration

- 45 minutes

## Talking Points

1. This is the first end-to-end validation of all prior setup.
- Config, dataset, evaluator definitions, and auth converge here.

2. Evaluation runs are asynchronous.
- Polling and terminal status handling are expected behavior.

3. Result counts are a starting signal, not full diagnosis.
- Use report links for deeper error analysis.

## Facilitation Flow

1. Run setup cell to create `openai_client` and load rows.
2. Run schema and evaluation creation cell.
3. Run evaluation launch and polling cell.
4. Have teams share run status and report URL.

## Questions To Ask Participants

- What status values indicate a terminal run state?
- Which metric result surprised you and why?
- If run failed, what evidence is in report details?

## Common Misunderstandings

- Assuming queued status is an error.
- Forgetting required dataset fields before create call.

## Session Checkpoint

Each team has:

- A completed run.
- A captured report URL.
- Result counts documented.
