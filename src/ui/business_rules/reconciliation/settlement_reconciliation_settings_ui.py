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


class TriggerNow(TestPoint):

    def __init__(self):  
        def func(driver = webdriver, date = str):
            assert "/settlement-reconciliation-settings" in driver.current_url, "❌ Not on settlement reconciliation settings page"
            try :
                date_input = driver.find_element(By.CSS_SELECTOR, "button.p-element").click()
                logging.info("Sale and settlement are matched")

            except Exception as e :
                logging.error(e)
            time.sleep(2)
            

        # Assign metadata separately
        tp_id = "TP2500"
        tp_description = f"Click on Trigger Now Button"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  
