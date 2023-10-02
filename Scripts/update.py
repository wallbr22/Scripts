import subprocess

def check_windows_updates():
    try:
        # Get available updates
        get_updates_command = (
            "powershell.exe Get-WindowsUpdate -ListOnly"
        )
        updates = subprocess.run(
            get_updates_command, shell=True, check=True, text=True, capture_output=True
        )

        # Print the results
        print("Available Windows updates:\n")
        print(updates.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    check_windows_updates()
