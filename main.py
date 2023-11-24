"""Main function for running the program."""
import re
import glob
from .get_log_errors import ErrorLogProcessing
from .constants import REGEX_USERNAME_PATTERN

class MainClass: # pylint: disable=too-few-public-methods
    """Main class."""
    def _send_mail(self, user: str, error: str):
        """Send mail to the user."""
        print(f"Sending email to {user} with the error {error}")
        # should send email here

    def __init__(self):
        """Initialize the class."""
        self.error_log_processing = ErrorLogProcessing()

    def run(self):
        """Run the program."""
        unassociated_errors_found = False
        affected_users = {}
        manual_review = {}
        log_files = []
        log_file_folder = 'tests/system_logs'
        log_files = glob.glob(log_file_folder + "/*")
        for logfile in log_files: # Use of list and dictionary
            error_count, error_set, warning_set= self.error_log_processing.get_log_errors(logfile)
        if error_count > 1000:
            print(f"Error count is {error_count}. This is too high! Consider stopping the services.")

        if error_set is not None: # Use of Boolean
            # get user from the message IF possible
            for error in error_set:
                user_match = re.search(REGEX_USERNAME_PATTERN, error)
                if user_match:
                    user = user_match.group(1)
                    affected_users[user] = error
                else:
                    unassociated_errors_found = True
                    manual_review["unassociated_errors"] = []
                    manual_review["unassociated_errors"].append(error)
        if affected_users:
            print("The following users were affected:")
            for user, error in affected_users.items():
                try:
                    self._send_mail(user, error)
                    print(f"Email sent to {user} with error {error}")
                except Exception as e:
                    print(f"An error occurred while sending email to {user}: {e}")
                    manual_review["unassociated_errors"].append(error)
                    unassociated_errors_found = True
                
        if unassociated_errors_found:
            print("Unassociated or unhandled errors. Please review manually.")
            print(manual_review)
        else:
            print("No unassociated found!")
        
        if warning_set is not None:
            print("The following warnings were found:")
            for warning in warning_set:
                print(warning)
        

if __name__ == "__main__":
    main = MainClass()
    main.run()