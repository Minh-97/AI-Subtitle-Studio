from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List


REQUIRED_FILES = [
    "config",
    "config/system_config.json",
    "docs/architecture.md",
    "PROJECT_SPEC.md",
    "docs/configuration.md",
]

REQUIRED_SECTIONS = [
    "## Mục lục",
    "## 1. Tổng quan",
    "## 3. Các thành phần chính",
    "## 7. Checklist",
]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_configuration_setup(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()

    missing_files: List[str] = []
    missing_sections: List[str] = []
    errors: List[str] = []

    for relative_path in REQUIRED_FILES:
        file_path = root_path / relative_path
        if not file_path.exists():
            missing_files.append(relative_path)
            continue

        if relative_path == "docs/architecture.md" or relative_path == "PROJECT_SPEC.md":
            content = _read_text(file_path)
            normalized = content.lower()
            for section in REQUIRED_SECTIONS:
                if section.lower() not in normalized:
                    missing_sections.append(f"{relative_path}: {section}")

    config_path = root_path / "config" / "system_config.json"
    if not config_path.exists():
        errors.append("system_config.json is missing")
    else:
        config_data = json.loads(_read_text(config_path))
        required_parameters = [
            "input_dir",
            "output_dir",
            "temp_dir",
            "subtitle_duration_seconds",
            "language",
            "log_level",
        ]
        missing_parameters = [parameter for parameter in required_parameters if parameter not in config_data]
        if missing_parameters:
            errors.append(f"system_config.json missing parameters: {', '.join(missing_parameters)}")

    if not (root_path / "config").exists():
        errors.append("config directory is missing")

    parameters = []
    if config_path.exists():
        config_data = json.loads(_read_text(config_path))
        parameters = list(config_data.keys())

    is_valid = not missing_files and not missing_sections and not errors

    return {
        "is_valid": is_valid,
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "errors": errors,
        "parameters": parameters,
    }


if __name__ == "__main__":
    import json

    result = validate_configuration_setup(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
