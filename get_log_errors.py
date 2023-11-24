"""Class for error log processing."""

class ErrorLogProcessing:
    """Class for error log processing."""
    def __init__(self):
        self.error_count: int = 0
        self.warning_count: int = 0
        self.error_messages: set = set() # use of set
        self.warning_messages: set = set()

    def get_log_errors(self, log_info: dict) -> tuple[int, set, set]:
        """Get the errors from the log file."""
        try:
            assert log_info['path'] is not None
            log_path = log_info['path']
            # Open the log file for reading
            with open(log_path, 'r') as log_file:
                # Read each line in the log file
                for line in log_file:
                    # Check if the line contains the word "Error"
                    if "error" in line.lower():
                        self.error_count += 1
                        self.error_messages.add(line.strip())
                    elif "warning" in line.lower():
                        self.warning_count += 1
                        self.warning_messages.add(line.strip())  

        except FileNotFoundError:
            print(f"Log file not found at {log_path}")
            return 0, set()
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0, set()
        return self.error_count,  self.error_messages, self.warning_messages # Use of tuple
        

