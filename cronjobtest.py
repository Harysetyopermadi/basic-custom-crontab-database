import subprocess
import platform

if __name__ == "__main__":
    # List of script paths
    script_paths = ["D:/Python/cronjob/test2.py", "D:/Python/cronjob/test1.py"]

    # Run the scripts in the background
    processes = []
    for path in script_paths:
        if platform.system() == "Windows":
            command = ["start", "python", path]
        else:
            command = ["nohup", "python", path, "&"]
        processes.append(subprocess.Popen(command, shell=True))

    # Wait for all processes to finish
    for process in processes:
        process.wait()

    print("All processes have finished")
