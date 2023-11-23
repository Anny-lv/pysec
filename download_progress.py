"""Download file from input URL with progress tracking that are animals."""
import urllib.request
import os
import sys
import time
import random

def download_file(url, destination):
    animals = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯"]

    def report_hook(count, block_size, total_size):
        """Callback function to track the download progress."""
        download_percent = int(count * block_size * 100 / total_size)
        animal = random.choice(animals)
        animal_speed = min(20, max(1, 20 - download_percent // 5))
        sys.stdout.write(f"\rDownloading... [{' ' * download_percent}{animal}{' ' * (100 - download_percent)}] {download_percent}%")
        sys.stdout.flush()
        time.sleep(0.1 / animal_speed)  # Adjust the sleep duration for dancing speed

    try:
        # Download the file with progress tracking
        urllib.request.urlretrieve(url, destination, reporthook=report_hook)
        print("\nDownload completed! File saved in 'downloads' folder.")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    # Input the file URL
    file_url = input("Enter the file URL: ")

    # Validate the URL and exit if invalid
    if not file_url.startswith("http"):
        print("Invalid URL. Please enter a valid HTTP or HTTPS URL.")
        sys.exit(1)

    # Create a "downloads" folder if it doesn't exist
    downloads_folder = os.path.join(os.getcwd(), "downloads")
    os.makedirs(downloads_folder, exist_ok=True)

    # Construct the full path for the downloaded file
    file_name = os.path.basename(file_url)
    save_path = os.path.join(downloads_folder, file_name)

    # Download the file and monitor the progress
    download_file(file_url, save_path)
