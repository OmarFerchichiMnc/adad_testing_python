import subprocess
import threading
import logging
from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
import time
import os


class BastionSSMForward(TestPoint):
    def __init__(self):
        
        def func(driver=webdriver):
            
            try:
                logging.info("🔎 Fetching Bastion instance ID...")
                # Get running bastion ID
                bastion_id = subprocess.check_output([
                    "aws", "ec2", "describe-instances",
                    "--filters", "Name=tag:Name,Values=adad-ec2-bastion",
                    "--query", "Reservations[].Instances[?State.Name=='running'].InstanceId",
                    "--output", "text",
                    "--region", "eu-west-1",
                    "--profile", "default"
                ], text=True).strip()

                if not bastion_id:
                    raise RuntimeError("❌ No running bastion instance found.")

                logging.info(f"✅ Found Bastion ID: {bastion_id}")

                # Function to run SSM in background
                def start_port_forward():
                    try:
                        logging.info("🚀 Starting SSM Port Forwarding session in background...")
                        subprocess.run([
                            "aws", "ssm", "start-session",
                            "--target", bastion_id,
                            "--region", "eu-west-1",
                            "--document-name", "AWS-StartPortForwardingSessionToRemoteHost",
                            "--parameters",
                            '{"portNumber":["2022"],"localPortNumber":["2022"],"host":["10.10.2.175"]}',
                            "--profile", "default"
                        ], check=True)
                    except subprocess.CalledProcessError as e:
                        logging.error(f"❌ AWS CLI error in background: {e}")
                    except Exception as e:
                        logging.error(f"❌ Unexpected error in background: {e}")

                # Start in a daemon thread so it does not block tests
                thread = threading.Thread(target=start_port_forward, daemon=True)
                thread.start()
                logging.info("✅ SSM Port Forwarding started in background")

            except subprocess.CalledProcessError as e:
                logging.error(f"❌ AWS CLI error: {e}")
                raise
            except Exception as e:
                logging.error(f"❌ Unexpected error: {e}")
                raise

        # Metadata
        tp_id = "TP0005"
        tp_description = "Start SSM Port Forwarding to Bastion (non-blocking)"
        tkt_id = "*****"
        tp_status = "ready"

        # Initialize base TestPoint
        super().__init__(
            id=tp_id,
            description=tp_description,
            func=func,
            ticket_id=tkt_id,
            status=tp_status,
            execution="failed"
        )

class KillBastionSSM(TestPoint):
    def __init__(self):
        
        def func(driver=webdriver):
            time.sleep(2)
            try:
                logging.info("🛑 Killing any running SSM Port Forwarding sessions...")
                # Find aws ssm start-session processes
                result = subprocess.run(
                    ["pgrep", "-f", "aws ssm start-session"],
                    capture_output=True,
                    text=True
                )
                pids = result.stdout.strip().split("\n")
                
                if not pids or pids == [""]:
                    logging.info("✅ No running SSM Port Forwarding sessions found.")
                    return
                
                # Kill all matching processes
                for pid in pids:
                    subprocess.run(["kill", "-9", pid])
                    logging.info(f"✅ Killed SSM session process with PID {pid}")

            except Exception as e:
                logging.error(f"❌ Error while killing SSM session: {e}")
                raise

        # Metadata
        tp_id = "TP0006"
        tp_description = "Kill all running SSM Port Forwarding sessions"
        tkt_id = "*****"
        tp_status = "ready"

        # Initialize base TestPoint
        super().__init__(
            id=tp_id,
            description=tp_description,
            func=func,
            ticket_id=tkt_id,
            status=tp_status,
            execution="failed"
        )

class PrepareUpload(TestPoint):
    def __init__(self, file_path, adad_file_path, file_name_to_put, mput='*.csv'):
        
        def func(driver=webdriver):
            logging.info("🔧 Preparing file upload...")

            # === Step 1: Validate local file path ===
            if not os.path.exists(file_path):
                logging.error("❌ Local path does not exist: %s", file_path)
                raise FileNotFoundError(f"Local path not found: {file_path}")
            logging.info("✅ Local path exists: %s", file_path)

            # === Step 2: Validate remote path ===
            if not adad_file_path or not isinstance(adad_file_path, str):
                logging.error("❌ Invalid remote path: %s", adad_file_path)
                raise ValueError("Remote path is invalid")
            logging.info("✅ Remote path is valid: %s", adad_file_path)

            # === Step 3: Check file to put ===
            full_file = os.path.join(file_path, file_name_to_put)
            if not os.path.exists(full_file):
                logging.error("❌ File to upload does not exist: %s", full_file)
                raise FileNotFoundError(f"File not found: {full_file}")
            logging.info("✅ File ready for upload: %s", full_file)

            logging.info("PrepareUpload TestPoint finished ✅")
            time.sleep(1)

        tp_id = "TP1001"
        tp_description = "Validate local and remote paths for SFTP upload"
        tkt_id = "*****"
        tp_status = "ready"

        super().__init__(
            id=tp_id,
            description=tp_description,
            func=func,
            ticket_id=tkt_id,
            status=tp_status,
            execution="failed"
        )

class ExecuteUpload(TestPoint):
    def __init__(self, file_path, adad_file_path, file_name_to_put, mput='*.csv'):
        
        def func(driver=webdriver):
            logging.info("🚀 Executing file upload via SFTP...")

            host = "localhost"
            port = "2022"
            username = "sftp_user_8X_staging"
            password = "3c1NIT0xj0VxMIs5"

            # Generate SFTP commands
            sftp_commands = f"""
lcd {file_path}
cd {adad_file_path}
put {file_name_to_put}
bye
"""

            logging.debug("Generated SFTP commands:\n%s", sftp_commands.strip())
            time.sleep(2)
            # Run SFTP upload
            result = subprocess.run(
                [
                    "sshpass", "-p", password,
                    "sftp",
                    "-o", "StrictHostKeyChecking=no",
                    "-o", "UserKnownHostsFile=/dev/null",  # ignore known_hosts
                    "-P", port,
                    f"{username}@{host}"
                ],
                input=sftp_commands,
                text=True,
                capture_output=True
            )

            if result.returncode != 0:
                logging.error("❌ SFTP failed with code %s\n%s", result.returncode, result.stderr)
                raise AssertionError(result.stderr)

            logging.info("✅ Files uploaded successfully:\n%s", result.stdout.strip())
            time.sleep(2)

        tp_id = "TP1002"
        tp_description = "Execute SFTP upload to /adad/8X/Sale/GLOBAL"
        tkt_id = "*****"
        tp_status = "ready"

        super().__init__(
            id=tp_id,
            description=tp_description,
            func=func,
            ticket_id=tkt_id,
            status=tp_status,
            execution="failed"
        )

class WaitForFileInjection(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            logging.info("⏰ Waiting for two minutes for the ingestion")
            time.sleep(120)
            logging.info("🕒 Done waiting")


        # Assign metadata separately
        tp_id = "TP0004"
        tp_description = f"Wait for file injection"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution="failed")  

class InjectFile(TestPoint):
    """Main orchestrator testpoint that runs all the smaller ones in correct order."""
    def __init__(self, file_path, adad_file_path, file_name_to_put, mput="*.csv"):

        def func(driver=webdriver):
            logging.info("🚀 Starting InjectFile.func execution")
            time.sleep(1)
            t1 = BastionSSMForward()
            t1.run(driver)
            t2 = PrepareUpload(file_path,adad_file_path,file_name_to_put,mput)
            t2.run(driver)
            t3 = ExecuteUpload(file_path,adad_file_path,file_name_to_put,mput)
            t3.run(driver)
            t4 = KillBastionSSM()
            t4.run(driver)
            t5 = WaitForFileInjection()
            t5.run(driver)
        tp_id = "TP1002"
        tp_description = "Execute SFTP upload"
        tkt_id = "*****"
        tp_status = "ready"
        super().__init__(
            id=tp_id,
            description=tp_description,
            func=func,
            ticket_id=tkt_id,
            status=tp_status,
            execution="failed"
        )





