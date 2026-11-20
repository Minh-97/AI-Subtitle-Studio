from __future__ import annotations

from pathlib import Path
from typing import Dict, List


REQUIRED_FILES = [
    "docs/architecture.md",
    "docs/translation_rules.md",
    "docs/timing_alignment.md",
]

REQUIRED_SECTIONS = [
    "## Mục lục",
    "## 1. Tổng quan",
    "## 3. Quy tắc đồng bộ",
    "## 5. Checklist",
]

REQUIRED_TIMING_RULES = ["sync_rules", "time_offset_handling", "pause_handling"]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_timing_alignment_setup(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()

    missing_files: List[str] = []
    missing_sections: List[str] = []
    errors: List[str] = []

    for relative_path in REQUIRED_FILES:
        file_path = root_path / relative_path
        if not file_path.exists():
            missing_files.append(relative_path)
            continue

        if relative_path == "docs/timing_alignment.md":
            content = _read_text(file_path)
            normalized = content.lower()
            for section in REQUIRED_SECTIONS:
                if section.lower() not in normalized:
                    missing_sections.append(f"{relative_path}: {section}")

    timing_doc_path = root_path / "docs" / "timing_alignment.md"
    if timing_doc_path.exists():
        content = _read_text(timing_doc_path)
        normalized = content.lower()
        for rule in REQUIRED_TIMING_RULES:
            if rule not in normalized:
                errors.append(f"timing alignment doc missing rule: {rule}")

    is_valid = not missing_files and not missing_sections and not errors

    return {
        "is_valid": is_valid,
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "errors": errors,
        "timing_rules": REQUIRED_TIMING_RULES,
    }


if __name__ == "__main__":
    import json

    result = validate_timing_alignment_setup(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
