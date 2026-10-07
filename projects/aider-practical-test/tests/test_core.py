"""Tests for core module."""

import unittest
import tempfile
import os
import json

from followup.core import validate_record, new_record, mark_done, mark_record_done
from followup.storage import load_records, save_records


class TestValidateRecord(unittest.TestCase):
    """Tests for validate_record function."""

    def test_valid_record(self):
        """Valid record should pass validation."""
        record = {
            "id": "test-id",
            "customer": "Test Customer",
            "channel": "email",
            "due_date": "2024-01-15",
            "status": "pending",
            "note": "Test note",
        }
        self.assertIsNone(validate_record(record))

    def test_invalid_channel(self):
        """Invalid channel should raise ValueError."""
        record = {
            "id": "test-id",
            "customer": "Test Customer",
            "channel": "invalid_channel",
            "due_date": "2024-01-15",
            "status": "pending",
            "note": "Test note",
        }
        with self.assertRaises(ValueError):
            validate_record(record)

    def test_invalid_date_format(self):
        """Invalid date format should raise ValueError."""
        record = {
            "id": "test-id",
            "customer": "Test Customer",
            "channel": "email",
            "due_date": "2024-13-45",
            "status": "pending",
            "note": "Test note",
        }
        with self.assertRaises(ValueError):
            validate_record(record)


class TestNewRecord(unittest.TestCase):
    """Tests for new_record function."""

    def test_creates_valid_record(self):
        """new_record should create a valid record."""
        record = new_record("Customer A", "whatsapp", "2024-01-20", "Follow up on invoice")
        
        self.assertEqual(record["customer"], "Customer A")
        self.assertEqual(record["channel"], "whatsapp")
        self.assertEqual(record["due_date"], "2024-01-20")
        self.assertEqual(record["status"], "pending")
        self.assertEqual(record["note"], "Follow up on invoice")
        self.assertTrue(len(record["id"]) > 0)


class TestMarkDone(unittest.TestCase):
    """Tests for mark_done function."""

    def test_mark_done_does_not_mutate_input(self):
        """mark_done should not mutate the input record."""
        original = {
            "id": "test-id",
            "customer": "Test Customer",
            "channel": "email",
            "due_date": "2024-01-15",
            "status": "pending",
            "note": "Test note",
        }
        original_copy = original.copy()
        
        result = mark_done(original)
        
        self.assertEqual(result["status"], "pending")
        self.assertEqual(original["status"], "pending")
        self.assertIsNot(result, original)

    def test_mark_record_done_updates_status(self):
        """mark_record_done should update status to done."""
        original = {
            "id": "test-id",
            "customer": "Test Customer",
            "channel": "email",
            "due_date": "2024-01-15",
            "status": "pending",
            "note": "Test note",
        }
        
        result = mark_record_done(original)
        
        self.assertEqual(result["status"], "done")
        self.assertEqual(original["status"], "pending")
        self.assertIsNot(result, original)


class TestStorage(unittest.TestCase):
    """Tests for storage module."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_db.json")

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_missing_file_returns_empty(self):
        """Missing file should return empty list."""
        records = load_records("/nonexistent/path/file.json")
        self.assertEqual(records, [])

    def test_save_load_round_trip(self):
        """Save and load should preserve data."""
        records = [
            {
                "id": "record-1",
                "customer": "Customer A",
                "channel": "email",
                "due_date": "2024-01-15",
                "status": "pending",
                "note": "Note 1",
            },
            {
                "id": "record-2",
                "customer": "Customer B",
                "channel": "whatsapp",
                "due_date": "2024-01-16",
                "status": "done",
                "note": "Note 2",
            },
        ]
        
        save_records(self.test_file, records)
        loaded = load_records(self.test_file)
        
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["id"], "record-1")
        self.assertEqual(loaded[1]["id"], "record-2")


if __name__ == "__main__":
    unittest.main()
