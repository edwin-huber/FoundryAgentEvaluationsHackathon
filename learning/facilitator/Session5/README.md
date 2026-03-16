# Session 5 Facilitator Guide: GitLab CI Integration

## Session Outcome

Participants configure GitLab CI to run cloud evaluations and enforce quality gates automatically.

## Suggested Duration

- 45 minutes

## Talking Points

1. CI transforms evaluation into a repeatable gate.
- This is the shift from manual testing to continuous enforcement.

2. Secret handling must be done in CI variables.
- Never hardcode credentials in pipeline YAML.

3. Gate failures are expected and useful.
- A failed pipeline is feedback, not just a blocker.

4. Keep run output concise and actionable.
- Summary JSON plus key pass/fail log lines are enough.

## Facilitation Flow

1. Show template from notebook and explain each pipeline step.
2. Have teams copy template to `.gitlab-ci.yml`.
3. Verify required CI/CD variables are configured.
4. Trigger pipeline and review logs together.
5. Explain how thresholds map to job exit code.

## Questions To Ask Participants

- Which variable is most often misconfigured in your team setup?
- What should cause pipeline failure versus warning-only behavior?
- How will you retain evaluation artifacts for audits?

## Common Misunderstandings

- Missing dataset file in repository path used by CI.
- Assuming successful script execution always means quality gate pass.

## Session Checkpoint

Each team demonstrates:

- A pipeline run that executes evaluation script.
- Clear pass/fail behavior tied to thresholds.
