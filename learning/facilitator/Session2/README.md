# Session 2 Facilitator Guide: Environment Setup and SDK Initialization

## Session Outcome

Participants can authenticate with Entra credentials, validate config, and connect to Foundry programmatically.

## Suggested Duration

- 35 minutes

## Talking Points

1. Environment issues are the most common blocker in CI later.
- Local parity with CI credentials is critical.

2. `DefaultAzureCredential` resolves multiple auth sources.
- Show why explicit service principal variables avoid ambiguity.

3. Validate early, fail fast.
- `validate_config` catches missing settings before runtime.

## Facilitation Flow

1. Walk participants through venv and requirements install.
2. Confirm required environment variables are set.
3. Run notebook connectivity check.
4. Run token acquisition cell and explain sanitized claims output.

## Questions To Ask Participants

- Which credential source is currently being used by `DefaultAzureCredential`?
- If CI fails auth, what local check can you run first?
- Do you see at least one agent in your project response?

## Common Misunderstandings

- Forgetting `PROJECT_ENDPOINT` or `MODEL_DEPLOYMENT_NAME`.
- Assuming token acquisition means project access permissions are correct.

## Session Checkpoint

Each team can produce:

- Successful `run_basic_connectivity_check()` output.
- Successful Entra token check output.
