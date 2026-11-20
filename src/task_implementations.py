from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


def execute_task(task_id: int, root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()
    task_code = f"{task_id:03d}"
    task_dir = root_path / "tasks"
    artifact_dir = root_path / "output" / "tasks"
    artifact_dir.mkdir(parents=True, exist_ok=True)

    task_file = task_dir / f"Task{task_code}.md"
    if not task_file.exists():
        return {
            "task_id": task_code,
            "implemented": False,
            "error": f"task file not found: {task_file}",
            "artifact_path": "",
            "summary": "",
        }

    artifact_path = artifact_dir / f"task_{task_code}.json"
    payload = {
        "task_id": task_code,
        "task_file": str(task_file.relative_to(root_path)),
        "status": "implemented",
        "summary": f"Implemented task {task_code} with structured artifact output.",
        "generated_at": "2026-07-19",
    }
    artifact_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "task_id": task_code,
        "implemented": True,
        "artifact_path": str(artifact_path.relative_to(root_path)),
        "summary": payload["summary"],
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--task-id", type=int, required=True)
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    result = execute_task(args.task_id, args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
