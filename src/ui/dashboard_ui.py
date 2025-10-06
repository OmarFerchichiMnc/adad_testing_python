from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class DashboardUISaleFilterDateRange(TestPoint):
    def __init__(self, date ):   
        def func(driver ):
            assert "dashboard" in driver.current_url, "❌ Not on dashboard page"
            try : 
                date_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-dashboard/div/div/div[2]/adad-frontend-date-range/div/div/p-calendar/span/button"))
    )
                date_input.click()
                logging.info("✅ Date input clicked")

                time.sleep(2)

                # Wait for clear button and click it
                clear_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/button[2]"))
                )
                clear_btn.click()
                logging.info("✅ Clear button clicked")

                # Check if clear_btn is active
                if clear_btn == driver.switch_to.active_element:
                    logging.info("✅ Clear button is now focused")
                else:
                    logging.warning("⚠️ Clear button did not get focus")

                time.sleep(2)

                # Re-locate the date input after clearing
                date_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-dashboard/div/div/div[2]/adad-frontend-date-range/div/div/p-calendar/span/input"))
                )

                # Send date
                date_input.send_keys(date)
                logging.info(f"✅ Date '{date}' entered")

                # Press Enter
                date_input.send_keys(Keys.ENTER)
                logging.info("✅ ENTER pressed to confirm date")

                time.sleep(2)

            except Exception as e :
                logging.error(e)
                raise AssertionError("❌ Failed to filter date")

        # Assign metadata separately
        tp_id = "TP0100"
        tp_description = f"Filter date range within dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  
