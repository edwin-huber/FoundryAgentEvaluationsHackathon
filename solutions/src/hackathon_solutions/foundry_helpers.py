import json
import time
from pathlib import Path
from typing import Any

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

from .config import FoundryConfig



def create_project_client(cfg: FoundryConfig) -> AIProjectClient:
    return AIProjectClient(
        endpoint=cfg.project_endpoint,
        credential=DefaultAzureCredential(),
        allow_preview=True,
    )


def create_openai_client(cfg: FoundryConfig):
    project_client = create_project_client(cfg)
    return project_client.get_openai_client()



def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items



def poll_until_completed(get_status_fn, run_id: str, sleep_seconds: int = 10, timeout_seconds: int = 900) -> Any:
    start = time.time()
    while True:
        status = get_status_fn(run_id)
        state = str(getattr(status, "status", "")).lower()

        if state in {"completed", "failed", "canceled", "cancelled"}:
            return status

        if time.time() - start > timeout_seconds:
            raise TimeoutError(f"Evaluation run {run_id} did not complete within {timeout_seconds} seconds")

        time.sleep(sleep_seconds)
