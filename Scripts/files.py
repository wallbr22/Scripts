import os

def get_size_of_folder(path='.'):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total

def list_folders_and_sizes(path):
    with os.scandir(path) as dir_entries:
        for entry in dir_entries:
            if entry.is_dir():
                folder_size = get_size_of_folder(entry.path) / (1024 * 1024)  # in MB
                print(f"{entry.name}: {folder_size:.2f} MB")

if __name__ == "__main__":
    path = 'C:\\Program Files (x86)'
    if os.path.exists(path):
        list_folders_and_sizes(path)
    else:
        print(f"The path '{path}' does not exist. Please ensure you have the correct path and permissions.")

