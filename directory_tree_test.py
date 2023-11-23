import unittest
import os
from directory_tree import get_file_stats, print_file_stats, get_stats_for_folder

class DirectoryTreeTests(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and files for testing
        self.temp_dir = "temp_dir"
        os.mkdir(self.temp_dir)
        self.temp_file1 = os.path.join(self.temp_dir, "file1.txt")
        self.temp_file2 = os.path.join(self.temp_dir, "file2.txt")
        with open(self.temp_file1, "w") as f1, open(self.temp_file2, "w") as f2:
            f1.write("This is file 1.")
            f2.write("This is file 2.")

    def tearDown(self):
        # Remove the temporary directory and files after testing
        os.remove(self.temp_file1)
        os.remove(self.temp_file2)
        os.rmdir(self.temp_dir)

    def test_get_file_stats(self):
        # Test the get_file_stats function
        stats = get_file_stats(self.temp_file1)
        self.assertIsInstance(stats, dict)
        self.assertIn("Size", stats)
        self.assertIn("Creation Time", stats)
        self.assertIn("Modification Time", stats)
        self.assertIn("Access Time", stats)

    def test_print_file_stats(self):
        # Test the print_file_stats function
        # Redirect stdout to a StringIO object for capturing the output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        print_file_stats(self.temp_file1)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check if the output contains the expected information
        output = captured_output.getvalue()
        self.assertIn("Stats for file:", output)
        self.assertIn("Size:", output)
        self.assertIn("Creation Time:", output)
        self.assertIn("Modification Time:", output)
        self.assertIn("Access Time:", output)

    def test_get_stats_for_folder(self):
        # Test the get_stats_for_folder function
        # Redirect stdout to a StringIO object for capturing the output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        get_stats_for_folder(self.temp_dir)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check if the output contains the expected information for each file
        output = captured_output.getvalue()
        self.assertIn("Stats for file:", output)
        self.assertIn("Size:", output)
        self.assertIn("Creation Time:", output)
        self.assertIn("Modification Time:", output)
        self.assertIn("Access Time:", output)
        self.assertIn("=" * 30, output)

if __name__ == "__main__":
    unittest.main()