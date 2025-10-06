import subprocess
import time



# Path to your shell script
sh_file = "/home/Omar.Ferchichi/Desktop/adad_testing_python/adad_testing/trying_injection/sftp 1.sh"


while True:
    try:
        print("Running script...")
        subprocess.run(["bash", sh_file], check=True)
        print("Script finished successfully. Restarting in 5 seconds...")
    except subprocess.CalledProcessError as e:
        print(f"Script crashed with code {e.returncode}. Restarting in 5 seconds...")
    except Exception as e:
        print(f"Unexpected error: {e}. Restarting in 5 seconds...")
    time.sleep(5)

