# Session 5: Integrating Foundry Evaluations with GitLab CI/CD
## Objective:
Transition from manual runs to an automated CI/CD pipeline. In this critical session, participants embed their evaluation into a GitLab CI workflow, so that agent evaluations can run on every code push or on a schedule, ensuring continuous quality checks.
## Procedure & Exercises:

### Create a Pipeline Configuration:
Teams will create a new file .gitlab-ci.yml at the root of their repository. We will provide a basic template for a pipeline with a single job (e.g., named “evaluate_agent”) that runs on a Python environment. 
Example template:
```yaml
stages:
  - evaluate

evaluate_agent:
  image: python:3.11
  stage: evaluate
  script:
    - pip install azure-ai-projects azure-identity azure-ai-evaluation  # Install SDK[4](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/cloud-evaluation?view=foundry-classic)
    - python run_evaluation.py       # Execute the evaluation script
  only:
    - main
```
This simple pipeline definition does the following: on commits to the main branch, it spins up a Python 3.11 container, installs the necessary Azure AI SDK packages, and runs the evaluation script prepared in earlier sessions. (In a real project, you might run this on merge to a staging branch or via a manual trigger, rather than every push – see Best Practices below.)

### Supply Environment Variables in CI:
For the pipeline to access your Azure resources, environment variables must be configured in GitLab CI. Using GitLab’s CI/CD settings, teams will add the same keys used in Session 2 (PROJECT_ENDPOINT, MODEL_ENDPOINT, MODEL_API_KEY, MODEL_DEPLOYMENT_NAME, etc.) as protected variables attached to the project or group. These will be automatically injected into the runtime environment of the CI job, so that the DefaultAzureCredential or the script can authenticate to Azure and Foundry services. (Alternatively, the script can load a separate config file or use GitLab’s encrypted file feature, but environment variables are straightforward for this hackathon.)

### Adapting the Evaluation Script for CI: 
The Python evaluation script from Session 4 needs a slight modification for CI usage. Specifically, teams should ensure it can run in a non-interactive environment. This means:

- No use of interactive authentication flows (rely on environment-based auth).
- The script should exit with an appropriate status. For instance, if we want the pipeline to **fail on poor performance**, the script can check the evaluation results against thresholds (e.g., if Task Adherence < 0.85, exit non-zero to fail the job). Otherwise, just exiting normally will mark the job as passed.
- Limit output: print a concise summary of results. The pipeline job logs can show key metrics, and detailed results remain in the Foundry portal.

### Run the Pipeline:
Once the .gitlab-ci.yml and script are in place, participants will push these changes to trigger the pipeline. They will monitor the pipeline in GitLab’s interface as it executes the evaluate_agent job. The job should install dependencies and then output logs indicating that an evaluation run was created and eventually completed. We expect the job to finish with a summary of evaluation scores (possibly retrieved via the SDK or simply a message that results are available in the portal).

### Troubleshooting:
If the pipeline fails, teams will debug with help from mentors. Common issues might include misconfigured environment variables, permission errors (e.g., if the service principal lacks rights to the project – ensure the Azure AD app is added to the project with the correct role), or pipeline YAML syntax errors. Solving these reinforces understanding of how the pieces fit together.

## Outcome:
By the end of this session, teams have a working CI/CD pipeline on GitLab that automatically runs their AI agent evaluations. This pipeline can be triggered on code changes or run on a schedule, providing continuous feedback on agent quality. The automation closes the loop: whenever the agent’s code or prompts are updated, the pipeline will run the standardized set of evaluators and report if the agent’s performance regresses or improves. Teams will have effectively created a CI/CD “testing” stage for AI agents, analogous to how traditional software tests are automated.