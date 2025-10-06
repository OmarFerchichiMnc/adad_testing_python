from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPointNavigateToAccountingJournal(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            accounting = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[8]/adad-frontend-sidebar-item/a/span")
            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"a.ng-tns-c35-129")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon ")
            
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[8]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the accounting journal sidebar item!")
            time.sleep(2)

            assert "/accounting-journal" in driver.current_url, "❌ Not on accounting journal page"
            execution_status = "passed"
            logging.info("-------Successfully Navigated to accounting journal page------")
        # Assign metadata separately
        tp_id = "TP0015"
        tp_description = f"Navigate to accounting journal page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToUnaccountedEvents(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            accounting = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[8]/adad-frontend-sidebar-item/a")
            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"a.ng-tns-c35-129")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon ")
            
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[8]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the unaccounting events sidebar item!")
            time.sleep(2)

            assert "/unaccounted-events" in driver.current_url, "❌ Not on unaccounting events page"
            
            logging.info("-------Successfully Navigated to unaccounting events page------")
        # Assign metadata separately
        tp_id = "TP0016"
        tp_description = f"Navigate to unaccounting events page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToImbalancedJournalEntries(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(5)
            accounting = driver.find_element(By.CSS_SELECTOR, "a.ng-tns-c35-129")
            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"a.ng-tns-c35-129")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon ")
            
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[8]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Imbalanced Journal Entries sidebar item!")
            time.sleep(2)

            assert "/imbalanced-items" in driver.current_url, "❌ Not on Imbalanced Journal Entries page"
            execution_status = "passed"
            logging.info("-------Successfully Navigated to Imbalanced Journal Entries page------")
        # Assign metadata separately
        tp_id = "TP0017"
        tp_description = f"Navigate to Imbalanced Journal Entries page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToTrialBalance(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(5)
            accounting = driver.find_element(By.CSS_SELECTOR, "a.ng-tns-c35-129")
            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"a.ng-tns-c35-129")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon ")
            
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[8]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the trial balance sidebar item!")
            time.sleep(2)

            assert "/trial-balance" in driver.current_url, "❌ Not on trial balance page"
            execution_status = "passed"
            logging.info("-------Successfully Navigated to trial balance page------")
        # Assign metadata separately
        tp_id = "TP0018"
        tp_description = f"Navigate to trial balance page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToPostToLedger(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(5)
            accounting = driver.find_element(By.CSS_SELECTOR, "a.ng-tns-c35-129")
            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"a.ng-tns-c35-129")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon ")
            
            
            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[8]/adad-frontend-sidebar-item/ul/li[5]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the post to ledger sidebar item!")
            time.sleep(2)

            assert "/post-to-ledger" in driver.current_url, "❌ Not on post to ledger page"
            execution_status = "passed"
            logging.info("-------Successfully Navigated to post to ledger page------")
        # Assign metadata separately
        tp_id = "TP0019"
        tp_description = f"Navigate to post to ledger page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  