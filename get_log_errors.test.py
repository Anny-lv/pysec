import unittest
from get_log_errors import ErrorLogProcessing

class TestErrorLogProcessing(unittest.TestCase):
    def setUp(self):
        self.error_log = ErrorLogProcessing()

    def test_get_log_errors_with_valid_log_file(self):
        log_info = {'path': 'path/to/valid/log/file.log'}
        error_count, error_messages, warning_messages = self.error_log.get_log_errors(log_info)
        self.assertEqual(error_count, 2)
        self.assertEqual(len(error_messages), 2)
        self.assertIn("Error: Something went wrong", error_messages)
        self.assertIn("Error: Another error occurred", error_messages)
        self.assertEqual(len(warning_messages), 1)
        self.assertIn("Warning: This is a warning message", warning_messages)

    def test_get_log_errors_with_invalid_log_file(self):
        log_info = {'path': 'path/to/invalid/log/file.log'}
        error_count, error_messages, warning_messages = self.error_log.get_log_errors(log_info)
        self.assertEqual(error_count, 0)
        self.assertEqual(len(error_messages), 0)
        self.assertEqual(len(warning_messages), 0)

    def test_get_log_errors_with_empty_log_file(self):
        log_info = {'path': 'path/to/empty/log/file.log'}
        error_count, error_messages, warning_messages = self.error_log.get_log_errors(log_info)
        self.assertEqual(error_count, 0)
        self.assertEqual(len(error_messages), 0)
        self.assertEqual(len(warning_messages), 0)

if __name__ == '__main__':
    unittest.main()