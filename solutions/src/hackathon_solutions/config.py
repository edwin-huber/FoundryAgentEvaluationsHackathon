import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class FoundryConfig:
    project_endpoint: str
    model_deployment_name: str
    agent_id: str | None
    dataset_name: str
    dataset_version: str



def load_config() -> FoundryConfig:
    load_dotenv()

    return FoundryConfig(
        project_endpoint=os.getenv("PROJECT_ENDPOINT", ""),
        model_deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME", ""),
        agent_id=os.getenv("AGENT_ID"),
        dataset_name=os.getenv("DATASET_NAME", "hackathon-eval-dataset"),
        dataset_version=os.getenv("DATASET_VERSION", "1"),
    )



def validate_config(cfg: FoundryConfig) -> None:
    required = {
        "PROJECT_ENDPOINT": cfg.project_endpoint,
        "MODEL_DEPLOYMENT_NAME": cfg.model_deployment_name,
    }

    missing = [name for name, value in required.items() if not value]
    if missing:
        raise ValueError(
            "Missing required environment variables: " + ", ".join(missing)
        )
