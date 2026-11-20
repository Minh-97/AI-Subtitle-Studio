from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

REQUIRED_TASKS = [f"Task{index:03d}.md" for index in range(1, 31)]
REQUIRED_SECTIONS = [
    "## Mục tiêu",
    "## Mô tả",
    "## Input",
    "## Output",
    "## API",
    "## Test",
    "## Điều kiện hoàn thành",
    "## Checklist",
]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_task_documents(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()
    tasks_dir = root_path / "tasks"

    missing_tasks: List[str] = []
    missing_sections: List[str] = []
    errors: List[str] = []
    task_files: List[str] = []

    if not tasks_dir.exists():
        errors.append("tasks directory is missing")
        return {
            "is_valid": False,
            "missing_tasks": REQUIRED_TASKS,
            "missing_sections": [],
            "errors": errors,
            "task_files": [],
            "tasks_checked": 0,
        }

    for task_name in REQUIRED_TASKS:
        task_path = tasks_dir / task_name
        if not task_path.exists():
            missing_tasks.append(task_name)
            continue

        task_files.append(f"tasks/{task_name}")
        content = _read_text(task_path)
        normalized = content.lower()

        for section in REQUIRED_SECTIONS:
            if section.lower() not in normalized:
                missing_sections.append(f"{task_name}: {section}")

        if "## mục tiêu" not in normalized:
            errors.append(f"{task_name}: missing title section")

    is_valid = not missing_tasks and not missing_sections and not errors

    return {
        "is_valid": is_valid,
        "missing_tasks": missing_tasks,
        "missing_sections": missing_sections,
        "errors": errors,
        "task_files": sorted(task_files),
        "tasks_checked": len(task_files),
    }


if __name__ == "__main__":
    import json

    result = validate_task_documents(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
