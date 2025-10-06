from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestPointNavigateToAlertManagement(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            alert_icon = driver.find_element(By.XPATH, "//span[text()='Alerts']/parent::a")
            if "active-menuitem" in alert_icon.get_attribute("class"):
                logging.info("Successfully clicked the data ingestion icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"i.ng-tns-c35-111:nth-child(3)")
                click_icon.click()
                logging.info("Successfully clicked the Alert icon ")



            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[3]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Alert management sidebar item!")
            time.sleep(2)

            assert "/alerts" in driver.current_url, "❌ Not on alerts management page"
            logging.info("-------Successfully Navigated to alerts management page------")
        # Assign metadata separately
        tp_id = "TP0002"
        tp_description = f"Navigate to Alert management page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  



class TestPointNavigateToReconciliationAlerts(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            alert_icon = driver.find_element(By.XPATH, "//span[text()='Alerts']/parent::a")
            if "active-menuitem" in alert_icon.get_attribute("class"):
                logging.info("Successfully clicked the data ingestion icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"i.ng-tns-c35-111:nth-child(3)")
                click_icon.click()
                logging.info("Successfully clicked the Alert icon ")

            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[3]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Reconciliation Alert sidebar item!")
            time.sleep(3)

            assert "/reconciliation-alerts" in driver.current_url, "❌ Not on reconciliation alerts page"
            logging.info("-------Successfully Navigated to areconciliation alerts page------")
        # Assign metadata separately
        tp_id = "TP0003"
        tp_description = f"Navigate to Reconciliation Alert page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  