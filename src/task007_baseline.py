from __future__ import annotations

from pathlib import Path
from typing import Dict, List


REQUIRED_FILES = [
    "docs/qa_rules.md",
    "docs/terminology.md",
    "docs/transcript_qa.md",
]

REQUIRED_SECTIONS = [
    "## Mục lục",
    "## 1. Tổng quan",
    "## 3. Tiêu chí đánh giá",
    "## 5. Checklist",
]

REQUIRED_QUALITY_CRITERIA = ["completeness", "continuity", "duplication", "grammar"]
REQUIRED_ERROR_CATEGORIES = ["major_error", "minor_error", "warning"]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_transcript_qa_setup(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()

    missing_files: List[str] = []
    missing_sections: List[str] = []
    errors: List[str] = []

    for relative_path in REQUIRED_FILES:
        file_path = root_path / relative_path
        if not file_path.exists():
            missing_files.append(relative_path)
            continue

        if relative_path == "docs/transcript_qa.md":
            content = _read_text(file_path)
            normalized = content.lower()
            for section in REQUIRED_SECTIONS:
                if section.lower() not in normalized:
                    missing_sections.append(f"{relative_path}: {section}")

    qa_doc_path = root_path / "docs" / "transcript_qa.md"
    if qa_doc_path.exists():
        content = _read_text(qa_doc_path)
        normalized = content.lower()
        for criterion in REQUIRED_QUALITY_CRITERIA:
            if criterion not in normalized:
                errors.append(f"transcript qa doc missing criterion: {criterion}")
        for category in REQUIRED_ERROR_CATEGORIES:
            if category not in normalized:
                errors.append(f"transcript qa doc missing error category: {category}")

    is_valid = not missing_files and not missing_sections and not errors

    return {
        "is_valid": is_valid,
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "errors": errors,
        "quality_criteria": REQUIRED_QUALITY_CRITERIA,
        "error_categories": REQUIRED_ERROR_CATEGORIES,
    }


if __name__ == "__main__":
    import json

    result = validate_transcript_qa_setup(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
