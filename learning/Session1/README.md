# Session 1 Learning Guide: Concepts and Evaluation Plan

## Goal

Understand what agentic evaluation measures and produce a practical evaluation plan you will use in later sessions.

## Inputs You Will Use

- Session brief in `Session1/Session1.md`
- Solution notebook `solutions/Session1/session1_concepts_and_plan.ipynb`

## Step-by-Step

1. Read the session objective and metric categories.
- Focus on three groups: agent behavior, quality, and safety.
- Identify why each group matters for your agent use case.

2. Open and run the Session 1 notebook.
- Run the cell that defines `evaluation_plan`.
- Review selected metrics:
  - agent behavior: `task_adherence`, `intent_resolution`, `tool_call_accuracy`
  - quality: `coherence`, `relevance`
  - safety: `violence`, `hate`

3. Confirm target thresholds.
- In the same plan, note minimum targets:
  - `task_adherence >= 0.85`
  - `coherence >= 0.85`
  - `relevance >= 0.85`

4. Adapt the plan to your team scenario.
- Decide which metrics are mandatory quality gates.
- Decide which metrics are informational only.

5. Save your final evaluation plan.
- Keep the metric list and thresholds available for Sessions 3-6.

## Checkpoint

You are done when you can answer:

- Which metrics represent behavior vs quality vs safety?
- Which three thresholds will block deployment?

## Expected Output Example

```python
evaluation_plan = {
    "agent_behavior": ["task_adherence", "intent_resolution", "tool_call_accuracy"],
    "quality": ["coherence", "relevance"],
    "safety": ["violence", "hate"],
    "target_thresholds": {
        "task_adherence": 0.85,
        "coherence": 0.85,
        "relevance": 0.85,
    },
}
```

## Troubleshooting

- If metrics feel too broad, keep the default set and refine in Session 6 after seeing real results.
- If your team disagrees on thresholds, start with `0.85` and adjust only after baseline runs.
