"""Tests for the download_progress module."""
import unittest
from unittest.mock import patch
from io import StringIO
import tempfile
import os
import shutil
from download_progress import download_file

class TestDownloadFile(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.test_dir)

    def test_download_file(self):
        file_url = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-embed-win32.zip"
        save_path = os.path.join(self.test_dir, "test_file.txt")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('time.sleep', return_value=None):
                download_file(file_url, save_path)

        # Check if progress is printed to stdout
        output = mock_stdout.getvalue()
        self.assertIn("Downloading...", output)
        self.assertIn("Download completed!", output)

    def test_invalid_url(self):
        """Test if an invalid URL is handled correctly."""
        invalid_url = "/test.com/test_file.txt"
        save_path = os.path.join(self.test_dir, "test_file.txt")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            download_file(invalid_url, save_path)

        # Check if an error message is printed to stdout
        output = mock_stdout.getvalue()
        self.assertIn("Error downloading file:", output)

if __name__ == '__main__':
    unittest.main()
