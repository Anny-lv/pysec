"""Script to connect to FTP servers and list files in the root directory. 
This app should be able to connect to multiple FTP servers at the same time. """
import ftplib
import threading
from queue import Queue

def ftp_worker(site, username, password, n_files):
    """Connect to FTP server and list files in the root directory."""
    try:
        with ftplib.FTP(site) as ftp:
            ftp.login(username, password) # login with test passwords
            files = ftp.nlst()[:n_files] if n_files > 0 else ftp.nlst() # list first n_files files
            print(f"Site: {site}, Root files: {files}")
    except Exception as e:
        print(f"Error accessing {site}: {e}")

def create_worker_threads(queue, n_files):
    threads = []
    for _ in range(3): # create 3 worker threads
        thread = threading.Thread(target=ftp_worker_thread, args=(queue, n_files))
        thread.start()
        threads.append(thread)
    return threads

def ftp_worker_thread(queue, n_files):
    while True:
        site_info = queue.get()
        if site_info is None:
            break
        ftp_worker(*site_info, n_files)

def main():
    n_files = 10 # number of files to list in root directory, we dont want to list all files

    ftp_sites_info = [
        ("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu"),
        ("test.rebex.net", "demo", "password"),
        ("speedtest.tele2.net", "anonymous", "anonymous"),
    ]

    queue = Queue()
    for site_info in ftp_sites_info:
        queue.put(site_info)

    threads = create_worker_threads(queue, n_files)

    queue.join() # wait for queue to be empty

    for _ in range(len(threads)):
        queue.put(None)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
