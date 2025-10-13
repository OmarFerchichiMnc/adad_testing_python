from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPointNavigateToAuditTrackSale(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(5)
            audit_track = driver.find_element(By.XPATH, "//span[text()='Audit Track']/parent::a")

            if "active-menuitem" in audit_track.get_attribute("class"):
                logging.info("Successfully clicked the audit track icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"i.ng-tns-c35-117:nth-child(3)")
                click_icon.click()
                logging.info("Successfully clicked the audit track icon ")
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[5]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a")
            sidebar_item.click()
            logging.info("Successfully clicked the audit track sidebar item!")
            time.sleep(2)

            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            logging.info("-------Successfully Navigated to audit track sale page------")
        # Assign metadata separately
        tp_id = "TP0006"
        tp_description = f"Navigate to audit track sale page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  


class TestPointNavigateToAuditTrackSettlement(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            audit_track = driver.find_element(By.XPATH, "//span[text()='Audit Track']/parent::a")

            if "active-menuitem" in audit_track.get_attribute("class"):
                logging.info("Successfully clicked the audit track icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"i.ng-tns-c35-117:nth-child(3)")
                click_icon.click()
                logging.info("Successfully clicked the audit track icon ")
            
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[5]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the audit track settlement sidebar item!")
            time.sleep(2)

            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track settlement page"
            logging.info("-------Successfully Navigated to audit track settlement page------")
        # Assign metadata separately
        tp_id = "TP0007"
        tp_description = f"Navigate to audit track settlement page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  