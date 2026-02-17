# Session 6: Results Interpretation and Best Practices Wrap-up
## Objective: 
Consolidate lessons learned and outline best practices for maintaining agent quality through continuous evaluation.

## Discussion and Analysis:
Each team will briefly present their pipeline and share any interesting findings from their agent’s evaluation results. We will discuss questions like: Which evaluator scores were good or bad, and why? How might they improve their agent based on the feedback? This reinforces the ultimate purpose of evaluation \- not just to get a number, but to drive iterative improvement of AI systems.

### Best Practices Highlighted:

We will conclude by emphasizing important takeaways for real-world use of these techniques:
- Automate but Be Selective: It’s usually unnecessary and costly to run full evaluations on every single code commit. A recommended practice is to run AI evaluations on a schedule (e.g., nightly) or on specific triggers like a release branch update or a manual trigger for engineers, rather than every push. This balances obtaining frequent feedback with controlling Azure OpenAI usage costs.
- Use Cloud Evaluations for Scale: We reiterate that running evaluations in the cloud is the preferred approach for CI pipelines. Cloud runs are more scalable and remove the burden of managing compute resources, enabling testing on larger datasets efficiently.
- Define Quality Gates: Teams should decide on quantitative thresholds for success. For example, require a minimum score on critical metrics (such as no more than X% of responses flagged as unsafe, or at least 90% coherence) before deploying to production. This can be implemented by parsing the evaluation results in the pipeline and failing the build if criteria aren’t met. Foundry’s framework allows setting such acceptance thresholds (e.g., 85% task adherence as a pass rate) to enforce quality gates in CI.
- Continuous Improvement: Encourage participants to integrate what they built during the hackathon into their regular development process. The pipeline can be extended to run on various branches (for example, run quick smoke-test evaluations on each merge request, and more exhaustive evaluations overnight). Additionally, after deployment, consider using Foundry’s continuous evaluation features to sample real production interactions and evaluate them automatically, thus catching any regressions or safety issues in live systems.

