from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestPointNavigateToCashForecast(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[2]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the cash forecast sidebar item!")
            time.sleep(2)

            assert "/cash-forecast" in driver.current_url, "❌ Not on cash forecast page"
            logging.info("-------Successfully Navigated to cash forecast page------")
        # Assign metadata separately
        tp_id = "TP001"
        tp_description = f"Navigate to cash forecast page"
        tkt_id= f"ADAD-0001"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

