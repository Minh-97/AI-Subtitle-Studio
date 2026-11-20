from __future__ import annotations

from pathlib import Path
from typing import Dict, List


REQUIRED_FILES = [
    "docs/translation_rules.md",
    "docs/terminology.md",
    "docs/translation_workflow.md",
]

REQUIRED_SECTIONS = [
    "## Mục lục",
    "## 1. Tổng quan",
    "## 3. Quy trình dịch thuật",
    "## 5. Checklist",
]

REQUIRED_TRANSLATION_RULES = ["technical_terms", "proper_names", "context"]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_translation_setup(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()

    missing_files: List[str] = []
    missing_sections: List[str] = []
    errors: List[str] = []

    for relative_path in REQUIRED_FILES:
        file_path = root_path / relative_path
        if not file_path.exists():
            missing_files.append(relative_path)
            continue

        if relative_path == "docs/translation_workflow.md":
            content = _read_text(file_path)
            normalized = content.lower()
            for section in REQUIRED_SECTIONS:
                if section.lower() not in normalized:
                    missing_sections.append(f"{relative_path}: {section}")

    translation_doc_path = root_path / "docs" / "translation_workflow.md"
    if translation_doc_path.exists():
        content = _read_text(translation_doc_path)
        normalized = content.lower()
        for rule in REQUIRED_TRANSLATION_RULES:
            if rule not in normalized:
                errors.append(f"translation doc missing rule: {rule}")

    is_valid = not missing_files and not missing_sections and not errors

    return {
        "is_valid": is_valid,
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "errors": errors,
        "translation_rules": REQUIRED_TRANSLATION_RULES,
    }


if __name__ == "__main__":
    import json

    result = validate_translation_setup(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
