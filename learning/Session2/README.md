# Session 2 Learning Guide: Environment Setup and SDK Initialization

## Goal

Set up Python dependencies, load project configuration, and verify authentication and Foundry connectivity.

## Inputs You Will Use

- Session brief in `Session2/Session2.md`
- Solution notebook `solutions/Session2/session2_environment_and_sdk.ipynb`
- Helpers in `solutions/src/hackathon_solutions/config.py` and `solutions/src/hackathon_solutions/evaluation_runner.py`

## Step-by-Step

1. Create and activate a virtual environment.

```bash
cd solutions
python3 -m venv .venv
source .venv/bin/activate
```

2. Install required packages.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Set environment variables.
- Required: `PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT_NAME`
- Authentication: `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`
- Optional: `AGENT_ID`, `DATASET_NAME`, `DATASET_VERSION`

4. Open and run Session 2 notebook Cell 2.
- This imports `load_config`, `validate_config`, and `run_basic_connectivity_check`.
- It also adds candidate source folders to `sys.path` so imports work from different working directories.

5. Run Session 2 notebook Cell 3.
- This calls `run_basic_connectivity_check()`.
- Expected output contains project endpoint, agent count, and discovered agent IDs.

6. Run Session 2 notebook Cell 4.
- This acquires an Entra token through `DefaultAzureCredential`.
- It prints sanitized claims (`aud`, tenant ID, client app ID, expiry).

## Checkpoint

You are done when all three are true:

- Config validation succeeds with no missing variable errors.
- Connectivity check returns agent metadata.
- Entra token acquisition succeeds.

## Expected Output Example

```json
{
  "project_endpoint": "https://<your-project-endpoint>",
  "agent_count": 1,
  "agent_ids": ["asst_..."]
}
```

## Troubleshooting

- `Missing required environment variables`: verify `.env` or shell exports.
- `DefaultAzureCredential` failure: confirm service principal values and tenant.
- Import failures for `hackathon_solutions`: rerun the path bootstrap cell.
