from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List


REQUIRED_FILES = [
    "docs/architecture.md",
    "docs/project_spec.md",
    "docs/configuration.md",
    "docs/input_handling.md",
]

REQUIRED_SECTIONS = [
    "## Mục lục",
    "## 1. Tổng quan",
    "## 3. Quy trình kiểm tra đầu vào",
    "## 5. Checklist",
]

REQUIRED_INPUT_TYPES = ["video", "audio"]
REQUIRED_METADATA_FIELDS = ["source_file", "file_type", "duration_seconds", "metadata"]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_input_handling_setup(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()

    missing_files: List[str] = []
    missing_sections: List[str] = []
    errors: List[str] = []

    for relative_path in REQUIRED_FILES:
        file_path = root_path / relative_path
        if not file_path.exists():
            missing_files.append(relative_path)
            continue

        if relative_path == "docs/input_handling.md":
            content = _read_text(file_path)
            normalized = content.lower()
            for section in REQUIRED_SECTIONS:
                if section.lower() not in normalized:
                    missing_sections.append(f"{relative_path}: {section}")

    input_doc_path = root_path / "docs" / "input_handling.md"
    if input_doc_path.exists():
        content = _read_text(input_doc_path)
        normalized = content.lower()
        for input_type in REQUIRED_INPUT_TYPES:
            if input_type not in normalized:
                errors.append(f"input doc missing supported input type: {input_type}")
        for field in REQUIRED_METADATA_FIELDS:
            if field not in normalized:
                errors.append(f"input doc missing metadata field: {field}")

    input_types = ["video", "audio"]
    metadata_fields = ["source_file", "file_type", "duration_seconds", "metadata"]

    is_valid = not missing_files and not missing_sections and not errors

    return {
        "is_valid": is_valid,
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "errors": errors,
        "input_types": input_types,
        "metadata_fields": metadata_fields,
    }


if __name__ == "__main__":
    import json

    result = validate_input_handling_setup(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
