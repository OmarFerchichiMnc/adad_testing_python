import json
import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.configuration.utils.utils import database_config
from src.testpoint.testpoint_main import TestPoint




#sftp running

import pytest
import subprocess
import time
import threading
import logging

def run_script_loop(sh_file):
    """Run the script in an infinite loop with restart logic."""
    while True:
        try:
            logging.info("Running script...")
            subprocess.run(["bash", sh_file], check=True)
            time.sleep(5)
            logging.info("Script started successfully. Restarting in 5 seconds...")
            
            
        except subprocess.CalledProcessError as e:
            logging.error(f"Script crashed with code {e.returncode}. Restarting in 5 seconds...")
        except Exception as e:
            logging.exception(f"Unexpected error: {e}. Restarting in 5 seconds...")
        time.sleep(5)


@pytest.fixture(scope="session", autouse=True)
def background_script():
    """Start the shell script loop once per pytest session."""
    sh_file = "/home/Omar.Ferchichi/Desktop/adad_testing_python/adad_testing/trying_injection/sftp 1.sh"

    thread = threading.Thread(target=run_script_loop, args=(sh_file,), daemon=True)
    thread.start()
    logging.info("SFTP script thread started.")
    yield
    logging.info("SFTP script thread stopped.")
    # No cleanup needed since thread is daemon=True



















# Initialize variable for the logs folder path
logs_folder_path = ""

def pytest_sessionstart(session):
    """Create a time-stamped log folder before the session starts."""
    global logs_folder_path
    date_str = datetime.now().strftime("%Y-%m-%d_%H")
    logs_folder_path = os.path.join("logs", date_str)

    # Ensure the log folder exists
    os.makedirs(logs_folder_path, exist_ok=True)

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Configure logging for each test in the correct log folder."""
    global logs_folder_path
    test_file = item.fspath.basename.replace(".py", "")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join(logs_folder_path, f"{test_file}_{timestamp}.log")

    # Remove previous logging handlers to avoid duplicates
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Set up logging to the log file
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info(f"--- Starting test: {item.name} ---")









#new-------------------------------------------------------------------------------------------------------------------------------
# conftest.py
import pytest
import requests
import os


@pytest.fixture(scope="session")
def auth_api():
    """Provides an authentication helper."""

    class AuthAPI:
        def authenticate(self, username: str, password: str):
            url = "https://security.staging.adad.io/realms/8X/protocol/openid-connect/token"  # replace Cypress.env('authUrl')
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            data = {
                "client_id": "adad-front",
                "grant_type": "password",
                "username": username,
                "password": password
            }

            response = requests.post(str(url), headers=headers, data=data, allow_redirects=True)
            response.raise_for_status()  # raise exception if status != 2xx
            return response.json()

    return AuthAPI()


@pytest.fixture(scope="session")
def auth_token(auth_api):
    """Returns an access token for tests."""
    username = os.getenv("AUTH_USERNAME", "meniar-qa")
    password = os.getenv("AUTH_PASSWORD", "Meniar123*")

    token_response = auth_api.authenticate(username, password)
    return token_response.get("access_token")


@pytest.fixture(scope="session")
def api_client(auth_token):
    """API client with Authorization header already set."""

    class APIClient:
        def __init__(self, token):
            self.base_url = os.getenv("API_BASE_URL", "https://8x.dev.adad.io/api/v1/bank-reconciliation-keys")
            self.headers = {"Authorization": f"Bearer {token}"}

        def get(self, endpoint, **kwargs):
            return requests.get(f"{self.base_url}{endpoint}", headers=self.headers, **kwargs)

        def post(self, endpoint, data=None, json=None, **kwargs):
            return requests.post(f"{self.base_url}{endpoint}", headers=self.headers, data=data, json=json, **kwargs)

        def put(self, endpoint, data=None, json=None, **kwargs):
            return requests.put(f"{self.base_url}{endpoint}", headers=self.headers, data=data, json=json, **kwargs)

        def delete(self, endpoint, **kwargs):
            return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers, **kwargs)

    return APIClient(auth_token)



import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options





@pytest.fixture(scope="session")
def driver():
    """Fixture to setup Chrome WebDriver, login, and return driver."""
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)


    driver.get("https://8x.staging.adad.io")
    time.sleep(3)

    # Click login button
    login_button = driver.find_element(By.CSS_SELECTOR, "#social-mnc-azure-ad")
    login_button.click()
    time.sleep(3)

    # Enter email
    driver.find_element(By.CSS_SELECTOR, "#i0116").send_keys("omar.ferchichi@mnc.aero")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
    time.sleep(2)

    # Enter password
    driver.find_element(By.CSS_SELECTOR, "#i0118").send_keys("M&C Adad 2025")  
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
    time.sleep(2)

    # Click yes on "Stay signed in?"
    driver.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
    time.sleep(2)

    logging.info("✅ Successfully logged in")

    yield driver   # <-- return driver to the test


    driver.quit()





import os
import subprocess
import time
import pytest
import psycopg2
from selenium import webdriver

# --- Constants ---
BASTION_TAG = "adad-ec2-bastion"
REGION = "eu-west-1"
LOCAL_PORT = "5555"
REMOTE_PORT = "5432"
REMOTE_HOST = "rds.staging.adad.internal"

# -------------------------------------------------------------------------
def get_bastion_instance_id():
    """Retrieve Bastion instance ID."""
    logging.info("🔍 Looking for Bastion instance...")
    os.environ["AWS_PROFILE"] = "default"

    try:
        bastion_id = subprocess.check_output([
            "aws", "ec2", "describe-instances",
            "--filters", f"Name=tag:Name,Values={BASTION_TAG}",
            "--query", "Reservations[].Instances[?State.Name=='running'].InstanceId",
            "--output", "text",
            "--region", REGION
        ], text=True).strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"❌ AWS CLI error: {e}")

    if not bastion_id:
        raise RuntimeError("❌ No running Bastion instance found!")

    logging.info(f"🛰️ Bastion instance found: {bastion_id}")
    return bastion_id


# -------------------------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def start_ssm_tunnel():
    """Start AWS SSM port forwarding session (autouse)."""
    bastion_id = get_bastion_instance_id()
    logging.info("🔗 Starting AWS SSM port forwarding session...")

    process = subprocess.Popen([
        "aws", "ssm", "start-session",
        "--target", bastion_id,
        "--region", REGION,
        "--document-name", "AWS-StartPortForwardingSessionToRemoteHost",
        "--parameters",
        f'{{"portNumber":["{REMOTE_PORT}"],"localPortNumber":["{LOCAL_PORT}"],"host":["{REMOTE_HOST}"]}}'
    ])

    logging.info("⏳ Waiting for tunnel to initialize...")
    time.sleep(5)
    logging.info("✅ SSM tunnel started.")

    yield
    logging.info("🧹 Closing SSM tunnel...")
    process.terminate()
    process.wait(timeout=5)
    logging.info("✅ Tunnel closed.")
























