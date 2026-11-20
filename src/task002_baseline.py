from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List


REQUIRED_FILES = [
    "README.md",
    "pyproject.toml",
    "requirements.txt",
    "docs/coding_rules.md",
    "docs/architecture.md",
]

REQUIRED_SECTIONS = [
    "## Mục lục",
    "## 1. Mục đích",
    "## 2. Nguyên tắc chung",
    "## 6. Quy trình kiểm thử",
    "## 8. Checklist",
]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _normalize(text: str) -> str:
    return text.lower()


def validate_environment_setup(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()

    missing_files: List[str] = []
    missing_sections: List[str] = []
    errors: List[str] = []

    for relative_path in REQUIRED_FILES:
        file_path = root_path / relative_path
        if not file_path.exists():
            missing_files.append(relative_path)
            continue

        if relative_path == "docs/coding_rules.md":
            content = _read_text(file_path)
            normalized = _normalize(content)
            for section in REQUIRED_SECTIONS:
                if section.lower() not in normalized:
                    missing_sections.append(f"{relative_path}: {section}")

    if not (root_path / "pyproject.toml").exists():
        errors.append("pyproject.toml is missing")
    else:
        pyproject_text = _read_text(root_path / "pyproject.toml")
        if "requires-python" not in pyproject_text:
            errors.append("pyproject.toml is missing requires-python")

    if not (root_path / "requirements.txt").exists():
        errors.append("requirements.txt is missing")
    else:
        requirements_text = _read_text(root_path / "requirements.txt")
        if "pytest" not in requirements_text:
            errors.append("requirements.txt is missing pytest")

    if not (root_path / "README.md").exists():
        errors.append("README.md is missing")
    else:
        readme_text = _read_text(root_path / "README.md")
        if "ai subtitle studio" not in _normalize(readme_text):
            errors.append("README.md is missing project title")

    dependencies = []
    if (root_path / "requirements.txt").exists():
        requirements_text = _read_text(root_path / "requirements.txt")
        dependency_lines = [line.strip() for line in requirements_text.splitlines() if line.strip() and not line.startswith("#")]
        dependencies = dependency_lines
        dependency_names = []
        for dependency in dependency_lines:
            dependency_name = re.split(r"[<>=!~\s\[]", dependency, maxsplit=1)[0]
            dependency_names.append(dependency_name)
        dependencies = dependency_names

    is_valid = not missing_files and not missing_sections and not errors

    return {
        "is_valid": is_valid,
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "errors": errors,
        "dependencies": dependencies,
    }


if __name__ == "__main__":
    import json

    result = validate_environment_setup(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
