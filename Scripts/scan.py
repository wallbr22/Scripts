import subprocess

def run_windows_defender_quick_scan():
    try:
        # Start the quick scan
        start_scan_command = "powershell.exe Start-MpScan -ScanType QuickScan"
        subprocess.run(start_scan_command, shell=True, check=True, text=True)
        print("Windows Defender quick scan has started.")

        # Wait for the scan to finish
        wait_scan_command = "powershell.exe Wait-MpScanJob"
        subprocess.run(wait_scan_command, shell=True, check=True, text=True)
        print("Windows Defender quick scan has finished.")

        # Get the scan results
        get_results_command = "powershell.exe Get-MpThreatDetection"
        results = subprocess.run(get_results_command, shell=True, check=True, text=True, capture_output=True)
        print("Windows Defender quick scan results:\n")
        print(results.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_windows_defender_quick_scan()
