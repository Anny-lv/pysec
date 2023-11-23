"""Script that travels trough a directory tree and prints the stats for each file in the tree with file stats."""
import os
import time

def get_file_stats(file_path):
    """Returns a dictionary with the stats for a file."""
    stat_info = os.stat(file_path)
    size = stat_info.st_size
    creation_time = time.ctime(stat_info.st_ctime)
    modification_time = time.ctime(stat_info.st_mtime)
    access_time = time.ctime(stat_info.st_atime)

    return {
        'Size': size,
        'Creation Time': creation_time,
        'Modification Time': modification_time,
        'Access Time': access_time
    }

def print_file_stats(file_path):
    """Prints the stats for a file."""
    stats = get_file_stats(file_path)
    print(f"Stats for file: {file_path}")
    for stat, value in stats.items():
        print(f"{stat}: {value}")
    print("=" * 30)  # Print a separator line between files

def get_stats_for_folder(folder_path):
    """Prints the stats for each file in a folder."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print_file_stats(file_path)

if __name__ == "__main__":
    # User input for the folder path
    folder_path = input("Enter the folder path to get stats for: ")

    if os.path.exists(folder_path):
        get_stats_for_folder(folder_path)
        print("List complete! ")
    else:
        print("Folder not found.")
