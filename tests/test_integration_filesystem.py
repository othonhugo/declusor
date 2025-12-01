import os
import shutil
import tempfile
import unittest
from unittest.mock import patch

from declusor.config import InvalidArgument
from declusor.util.file import load_file, load_library, load_payload


class TestFilesystemIntegration(unittest.TestCase):
    def setUp(self) -> None:
        self.test_dir = tempfile.mkdtemp()
        self.lib_dir = os.path.join(self.test_dir, "lib")
        self.scripts_dir = os.path.join(self.test_dir, "scripts")

        os.makedirs(self.lib_dir)
        os.makedirs(self.scripts_dir)

    def tearDown(self) -> None:
        shutil.rmtree(self.test_dir)

    def test_load_library_reads_files(self) -> None:
        """Test that load_library reads all .sh files from library directory."""

        # Create some dummy library files
        with open(os.path.join(self.lib_dir, "lib1.sh"), "wb") as f:
            f.write(b"content1")

        with open(os.path.join(self.lib_dir, "lib2.sh"), "wb") as f:
            f.write(b"content2")

        # Create a non-sh file, should be ignored
        with open(os.path.join(self.lib_dir, "readme.txt"), "wb") as f:
            f.write(b"ignored")

        # Patch the config paths
        with patch("declusor.util.file.LIBRARY_DIR", self.lib_dir):
            content = load_library()

            # Order is not guaranteed by scandir, so check presence
            self.assertIn(b"content1", content)
            self.assertIn(b"content2", content)
            self.assertNotIn(b"ignored", content)

            # Check separator
            self.assertTrue(b"\n\n" in content)

    def test_load_payload_reads_file(self) -> None:
        """Test that load_payload reads a specific payload file."""

        payload_name = "payload.sh"

        with open(os.path.join(self.scripts_dir, payload_name), "wb") as f:
            f.write(b"payload_content")

        with patch("declusor.util.file.SCRIPTS_DIR", self.scripts_dir):
            content = load_payload(payload_name)

            self.assertEqual(content, b"payload_content")

    def test_load_payload_errors(self) -> None:
        """Test that load_payload raises appropriate errors for invalid files."""

        with patch("declusor.util.file.SCRIPTS_DIR", self.scripts_dir):
            # Missing file
            with self.assertRaisesRegex(InvalidArgument, "file not found"):
                load_payload("missing.sh")

            # Wrong extension
            with self.assertRaisesRegex(InvalidArgument, "not supported"):
                load_payload("script.py")

    def test_load_file_absolute_path(self) -> None:
        """Test that load_file reads a file from an absolute path."""

        filepath = os.path.join(self.test_dir, "test.txt")

        with open(filepath, "wb") as f:
            f.write(b"data")

        content = load_file(filepath)

        self.assertEqual(content, b"data")
