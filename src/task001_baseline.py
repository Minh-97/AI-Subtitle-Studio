from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List


REQUIRED_DOCS = [
    "README.md",
    "docs/architecture.md",
    "docs/roadmap.md",
    "docs/coding_rules.md",
    "docs/translation_rules.md",
    "docs/qa_rules.md",
    "docs/terminology.md",
    "docs/project_spec.md",
]

CORE_DOCS = ["README.md", "docs/architecture.md", "docs/project_spec.md"]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _extract_project_name(text: str) -> str | None:
    title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()

    for line in text.splitlines():
        if "AI Subtitle Studio" in line:
            return "AI Subtitle Studio"
    return None


def validate_project_docs(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()

    missing_files: List[str] = []
    missing_sections: List[str] = []
    inconsistencies: List[str] = []
    errors: List[str] = []

    for relative_path in REQUIRED_DOCS:
        file_path = root_path / relative_path
        if not file_path.exists():
            missing_files.append(relative_path)
            continue

        content = _read_text(file_path)
        normalized = content.lower()

        if relative_path == "README.md":
            if not re.search(r"^#\s+", content, flags=re.MULTILINE):
                missing_sections.append("README.md: title heading")
            if "ai subtitle studio" not in normalized:
                missing_sections.append("README.md: project name")
        else:
            if "mục lục" not in normalized:
                missing_sections.append(f"{relative_path}: Mục lục")
            if "checklist" not in normalized:
                missing_sections.append(f"{relative_path}: Checklist")

    project_name = None
    if (root_path / "README.md").exists():
        project_name = _extract_project_name(_read_text(root_path / "README.md"))

    if project_name is None:
        errors.append("Unable to determine project name from README.md")

    if project_name:
        for core_doc in ["docs/architecture.md", "docs/project_spec.md"]:
            path = root_path / core_doc
            if path.exists():
                content = _read_text(path)
                if project_name not in content and project_name.lower() not in content.lower():
                    inconsistencies.append(f"{core_doc}: project name is not consistent")

    is_valid = not missing_files and not missing_sections and not inconsistencies and not errors

    return {
        "is_valid": is_valid,
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "inconsistencies": inconsistencies,
        "errors": errors,
        "project_name": project_name,
        "core_docs_checked": len(CORE_DOCS),
    }


if __name__ == "__main__":
    import json

    result = validate_project_docs(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
