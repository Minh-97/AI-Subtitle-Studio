from __future__ import annotations

from pathlib import Path
from typing import Dict, List


REQUIRED_FILES = [
    "docs/architecture.md",
    "docs/project_spec.md",
    "docs/preprocessing.md",
]

REQUIRED_SECTIONS = [
    "## Mục lục",
    "## 1. Tổng quan",
    "## 3. Quy trình tiền xử lý",
    "## 5. Checklist",
]

REQUIRED_MEDIA_TYPES = ["audio", "video"]
REQUIRED_INTERMEDIATE_OUTPUTS = ["preprocessed_audio.wav", "preprocessed_video.mp4"]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_preprocessing_setup(root: str | Path) -> Dict[str, object]:
    root_path = Path(root).resolve()

    missing_files: List[str] = []
    missing_sections: List[str] = []
    errors: List[str] = []

    for relative_path in REQUIRED_FILES:
        file_path = root_path / relative_path
        if not file_path.exists():
            missing_files.append(relative_path)
            continue

        if relative_path == "docs/preprocessing.md":
            content = _read_text(file_path)
            normalized = content.lower()
            for section in REQUIRED_SECTIONS:
                if section.lower() not in normalized:
                    missing_sections.append(f"{relative_path}: {section}")

    preprocessing_doc_path = root_path / "docs" / "preprocessing.md"
    if preprocessing_doc_path.exists():
        content = _read_text(preprocessing_doc_path)
        normalized = content.lower()
        for media_type in REQUIRED_MEDIA_TYPES:
            if media_type not in normalized:
                errors.append(f"preprocessing doc missing media type: {media_type}")
        for output_name in REQUIRED_INTERMEDIATE_OUTPUTS:
            if output_name not in normalized:
                errors.append(f"preprocessing doc missing intermediate output: {output_name}")

    is_valid = not missing_files and not missing_sections and not errors

    return {
        "is_valid": is_valid,
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "errors": errors,
        "media_types": REQUIRED_MEDIA_TYPES,
        "intermediate_outputs": REQUIRED_INTERMEDIATE_OUTPUTS,
    }


if __name__ == "__main__":
    import json

    result = validate_preprocessing_setup(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
