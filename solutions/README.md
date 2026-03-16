# Foundry Agent Evaluations Hackathon Solutions (Python + venv + Notebooks)

This folder contains runnable solution examples for each session in the hackathon.
Each session has its own folder and notebook so teams can work incrementally.

## Structure

- `Session1/` Concepts and evaluation planning notebook
- `Session2/` Environment setup and SDK initialization notebook
- `Session3/` Dataset prep and evaluator configuration notebook
- `Session4/` Cloud evaluation execution notebook
- `Session5/` GitLab CI integration notebook and pipeline template
- `Session6/` Results interpretation and quality gate notebook
- `src/hackathon_solutions/` Reusable Python helpers used by notebooks/scripts
- `data/` Sample JSONL datasets
- `templates/` CI/CD starter templates

## Quick Start

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
cp .env.example .env
```

Then set values in `.env`:
- `PROJECT_ENDPOINT`
- `MODEL_DEPLOYMENT_NAME`
- `AGENT_ID` (optional but recommended for agent evaluations)
- `AZURE_TENANT_ID`
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`

Authentication uses Microsoft Entra ID through `DefaultAzureCredential`.
The CI template is wired for service principal credentials via environment variables.  

Make sure that the service principal has the required data action `Microsoft.CognitiveServices/accounts/AIServices/agents/write`

It needs this to perform `POST /api/projects/{projectName}/openai/*` operations.  
For instructions on granting the necessary permissions, see https://aka.ms/FoundryPermissions.

4. Start Jupyter:

```bash
jupyter lab
```

5. Run notebooks in order:
- `Session1/session1_concepts_and_plan.ipynb`
- `Session2/session2_environment_and_sdk.ipynb`
- `Session3/session3_dataset_and_evaluators.ipynb`
- `Session4/session4_run_cloud_evaluation.ipynb`
- `Session5/session5_gitlab_ci_integration.ipynb`
- `Session6/session6_results_and_quality_gates.ipynb`

## Notes

- These examples are designed to be adapted to your own Foundry project and agent.
- Most SDK calls are wrapped in helper functions under `src/hackathon_solutions/` to keep notebooks concise.
- For CI, use `templates/gitlab-ci.yml` as a baseline and copy to repository root as `.gitlab-ci.yml`.
- The Session 4 and `scripts/run_cloud_evaluation.py` examples use the live API shape:
	- `project_client.get_openai_client().evals.create(...)`
	- `project_client.get_openai_client().evals.runs.create(...)`
	- `project_client.get_openai_client().evals.runs.retrieve(...)`
