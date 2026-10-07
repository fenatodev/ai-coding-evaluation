"""Storage operations for follow-up records."""

import json
from pathlib import Path

from .core import validate_record


def load_records(path: str) -> list[dict]:
    """Load records from a JSON file.

    Args:
        path: Path to the JSON file

    Returns:
        List of records, or empty list if file doesn't exist
    """
    path_obj = Path(path)

    if not path_obj.exists():
        return []

    try:
        with open(path_obj, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        return []


def save_records(path: str, records: list[dict]) -> None:
    """Save records to a JSON file.

    Args:
        path: Path to the JSON file
        records: List of records to save

    Validates every record before writing.
    Creates parent directory if needed.
    """
    # Create parent directory if needed
    path_obj = Path(path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)

    # Validate all records
    for record in records:
        validate_record(record)

    with open(path_obj, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
