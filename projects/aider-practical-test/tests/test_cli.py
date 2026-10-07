"""Tests for CLI module."""

import unittest
import tempfile
import os
import shutil
import subprocess
import sys

from followup.core import new_record, mark_record_done
from followup.storage import load_records, save_records


class TestCLIAdd(unittest.TestCase):
    """Tests for CLI add command."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_db.json")

    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)

    def test_add_creates_persisted_record(self):
        """Add command should create a persisted record."""
        cmd = [
            sys.executable, "-m", "followup",
            "--db", self.test_file,
            "add",
            "--customer", "Test Customer",
            "--channel", "email",
            "--due", "2024-01-20",
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        
        records = load_records(self.test_file)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["customer"], "Test Customer")
        self.assertEqual(records[0]["channel"], "email")
        self.assertEqual(records[0]["due_date"], "2024-01-20")
        self.assertEqual(records[0]["status"], "pending")


class TestCLIList(unittest.TestCase):
    """Tests for CLI list command."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_db.json")

    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)

    def test_list_filters_by_status(self):
        """List command should filter by status."""
        # Create test data
        records = [
            new_record("Customer A", "email", "2024-01-15", "Note A"),
            new_record("Customer B", "whatsapp", "2024-01-16", "Note B"),
        ]
        save_records(self.test_file, records)
        
        # Mark one as done
        records[0] = mark_record_done(records[0])
        save_records(self.test_file, records)
        
        # List only pending
        cmd = [
            sys.executable, "-m", "followup",
            "--db", self.test_file,
            "list",
            "--status", "pending",
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        
        # Should only show the pending record
        self.assertIn("Customer B", result.stdout)
        self.assertNotIn("Customer A", result.stdout)


class TestCLIDone(unittest.TestCase):
    """Tests for CLI done command."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_db.json")

    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)

    def test_done_changes_status(self):
        """Done command should change status to done."""
        # Create test data
        record = new_record("Test Customer", "email", "2024-01-20", "Note 1")
        save_records(self.test_file, [record])
        
        # Mark as done
        cmd = [
            sys.executable, "-m", "followup",
            "--db", self.test_file,
            "done",
            record["id"],
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        
        # Verify status changed
        records = load_records(self.test_file)
        self.assertEqual(records[0]["status"], "done")

    def test_done_with_unknown_id_exits_2(self):
        """Done command with unknown id should exit with code 2."""
        cmd = [
            sys.executable, "-m", "followup",
            "--db", self.test_file,
            "done",
            "unknown-id-123",
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)


class TestCLIStats(unittest.TestCase):
    """Tests for CLI stats command."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_db.json")

    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)

    def test_stats_counts_pending_done_total(self):
        """Stats command should count pending, done, and total."""
        # Create test data
        all_records = [
            new_record("Customer A", "email", "2024-01-15", "Note A"),
            new_record("Customer B", "whatsapp", "2024-01-16", "Note B"),
            new_record("Customer C", "phone", "2024-01-17", "Note C"),
        ]
        all_records[2] = mark_record_done(all_records[2])
        
        save_records(self.test_file, all_records)
        
        cmd = [
            sys.executable, "-m", "followup",
            "--db", self.test_file,
            "stats",
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        
        self.assertIn("pending=2", result.stdout)
        self.assertIn("done=1", result.stdout)
        self.assertIn("total=3", result.stdout)


if __name__ == "__main__":
    unittest.main()
