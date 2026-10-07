"""Follow-up management module."""

from .core import validate_record, new_record, mark_done, mark_record_done
from .storage import load_records, save_records

__all__ = [
    "validate_record",
    "new_record",
    "mark_done",
    "mark_record_done",
    "load_records",
    "save_records",
]
