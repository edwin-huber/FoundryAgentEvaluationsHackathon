from pathlib import Path

from .config import load_config, validate_config
from .foundry_helpers import create_project_client



def run_basic_connectivity_check() -> dict:
    cfg = load_config()
    validate_config(cfg)

    client = create_project_client(cfg)

    agents = list(client.agents.list())
    return {
        "project_endpoint": cfg.project_endpoint,
        "agent_count": len(agents),
        "agent_ids": [getattr(a, "id", None) for a in agents],
    }



def upload_dataset(file_path: str) -> dict:
    cfg = load_config()
    validate_config(cfg)

    client = create_project_client(cfg)
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    result = client.datasets.upload_file(
        name=cfg.dataset_name,
        version=cfg.dataset_version,
        file_path=str(path),
    )

    return {
        "dataset_name": cfg.dataset_name,
        "dataset_version": cfg.dataset_version,
        "dataset_id": getattr(result, "id", None),
    }


if __name__ == "__main__":
    print(run_basic_connectivity_check())
