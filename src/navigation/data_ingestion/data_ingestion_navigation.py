from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestPointNavigateToFileDashboard(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(4)
            data_ingestion = driver.find_element(By.XPATH, "//span[text()='Data Ingestion']/parent::a")

            if "active-menuitem" in data_ingestion.get_attribute("class"):
                logging.info("Successfully clicked the data ingestion icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"a.ng-tns-c35-114")
                click_icon.click()
                logging.info("Successfully clicked the data ingestion icon ")
            
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[4]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the File Dashboard sidebar item!")
            time.sleep(2)

            assert "/etl-files" in driver.current_url, "❌ Not on File Dashboard page"
            logging.info("-------Successfully Navigated to File Dashboard page------")
        # Assign metadata separately
        tp_id = "TP0004"
        tp_description = f"Navigate to File Dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution="failed")  



class TestPointNavigateToFailedTransactions(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            data_ingestion = driver.find_element(By.XPATH, "//span[text()='Data Ingestion']/parent::a")
            if "active-menuitem" in data_ingestion.get_attribute("class"):
                logging.info("Successfully clicked the data ingestion icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"a.ng-tns-c35-114")
                click_icon.click()
                logging.info("Successfully clicked the data ingestion icon ")

                
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[4]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Failed Transactions sidebar item!")
            time.sleep(2)
            logging.info(driver.current_url)
            assert "/failed-transactions" in driver.current_url, "❌ Not on Failed Transactions page"
            
            logging.info("-------Successfully Navigated to Failed Transactions page------")

        # Assign metadata separately
        tp_id = "TP0005"
        tp_description = f"Navigate to Failed Transactions page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  