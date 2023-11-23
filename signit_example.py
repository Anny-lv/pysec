"""Example of using signal to handle CTRL+C. """
import signal
import time
import sys

timer = 10 # Time can be adjusted to see the effect

def long_running_task():
    try:
        # Simulate a long-running task
        for i in range(timer):
            print(f"Task in progress: {i}")
            time.sleep(1)
    except KeyboardInterrupt: # CTRL+C pressed
        print("\nCTRL+C received. Exiting gracefully.")

def signal_handler(sig):
    print(f"\nSignal {sig} received. Exiting gracefully.")
    sys.exit(0)

if __name__ == "__main__":
    # Set up signal handler for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)

    # Execute the long-running task
    long_running_task()

    print("Program completed.")
