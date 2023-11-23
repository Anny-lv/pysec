"""Application that is using two threads to run two tasks concurrently."""
import threading
import time

task_range = 10  # Range can be adjusted to see the effect

def task_one():
    for i in range(task_range):
        print(f"Task One: {i}")
        time.sleep(1)

def task_two():
    for i in range(task_range):
        print(f"Task Two: {i}")
        time.sleep(1)

if __name__ == "__main__":
    # Create two threads
    thread_one = threading.Thread(target=task_one)
    thread_two = threading.Thread(target=task_two)

    # Start the threads
    thread_one.start()
    thread_two.start()

    # Wait for both threads to complete
    thread_one.join()
    thread_two.join()

    print("Main thread exiting.")
