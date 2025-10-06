from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



class TestPointNavigateToPendingItems(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            reconciliation = driver.find_element(By.XPATH, "//span[text()='Reconciliation']/parent::a")

            if "active-menuitem" in reconciliation.get_attribute("class"):
                logging.info("Successfully clicked the Reconciliation icon ")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/a/i[2]")
                click_icon.click()
                logging.info("Successfully clicked the Reconciliation icon ")

            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the pending items item!")
            time.sleep(2)

            assert "/pending-items" in driver.current_url, "❌ Not on pending items page"
            logging.info("-------Successfully Navigated to pending items page------")
        # Assign metadata separately
        tp_id = "TP0008"
        tp_description = f"Navigate to pending items page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToProvisionalMismatchedItems(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            reconciliation = driver.find_element(By.XPATH, "//span[text()='Reconciliation']/parent::a")

            if "active-menuitem" in reconciliation.get_attribute("class"):
                logging.info("Successfully clicked the Reconciliation icon ")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/a/i[2]")
                click_icon.click()
                logging.info("Successfully clicked the Reconciliation icon ")

            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Provisional Mismatched Items item!")
            time.sleep(2)

            assert "/pending-items" in driver.current_url, "❌ Not on pending items page"
            logging.info("-------Successfully Navigated to Provisional Mismatched Items page------")
        # Assign metadata separately
        tp_id = "TP0009"
        tp_description = f"Navigate to Provisional Mismatched Itemspage"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToInstallments(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            installments = driver.find_element(By.XPATH, "//span[text()='Reconciliation']/parent::a")

            if "active-menuitem" in installments.get_attribute("class"):
                logging.info("Successfully clicked the Reconciliation icon ")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/a/i[2]")
                click_icon.click()
                logging.info("Successfully clicked the Reconciliation icon ")

            time.sleep(2)
            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the installments item!")
            time.sleep(2)

            assert "/installments" in driver.current_url, "❌ Not on installments page"
            logging.info("-------Successfully Navigated to installments page------")
        # Assign metadata separately
        tp_id = "TP0010"
        tp_description = f"Navigate to installments page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMatchedItemsMatched(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            installments = driver.find_element(By.XPATH, "//span[text()='Reconciliation']/parent::a")

            if "active-menuitem" in installments.get_attribute("class"):
                logging.info("Successfully clicked the Reconciliation icon ")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/a/i[2]")
                click_icon.click()
                logging.info("Successfully clicked the Reconciliation icon ")

            time.sleep(2)


            mached_items = driver.find_element(By.XPATH, "//a[contains(@class,'ng-star-inserted')]//span[text()='Matched Items']")

            if "active-menuitem" in mached_items.get_attribute("class"):
                logging.info("Successfully clicked the Matched Items icon ")
            else:
                click_icon = driver.find_element(By.XPATH, "//a[contains(@class,'ng-star-inserted')]//span[text()='Matched Items']")
                click_icon.click()
                logging.info("Successfully clicked the Matched Items icon ")


            time.sleep(2)

            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the mached item!")
            time.sleep(2)

            assert "/matched-items" in driver.current_url, "❌ Not on Matched page"
            logging.info("-------Successfully Navigated to Matched page------")
        # Assign metadata separately
        tp_id = "TP0011"
        tp_description = f"Navigate to Matched page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToExceptions(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            installments = driver.find_element(By.XPATH, "//span[text()='Reconciliation']/parent::a")

            if "active-menuitem" in installments.get_attribute("class"):
                logging.info("Successfully clicked the Reconciliation icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/a/i[2]")
                click_icon.click()
                logging.info("Successfully clicked the Reconciliation icon **")

            time.sleep(2)

            try :
                mached_items = driver.find_element(By.XPATH, "//span[normalize-space()='Matched Items']/parent::a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in mached_items.get_attribute("class"):
                logging.info("Successfully clicked the Matched Items icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "//a[contains(@class,'ng-star-inserted')]//span[text()='Matched Items']")
                click_icon.click()
                logging.info("Successfully clicked the Matched Items icon --")


            time.sleep(3)

            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Exceptions item!")
            time.sleep(2)

            assert "matched-items/exceptions" in driver.current_url, "❌ Not on Exceptions page"
            logging.info("-------Successfully Navigated to Exceptions page------")
        # Assign metadata separately
        tp_id = "TP0012"
        tp_description = f"Navigate to Exceptions page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToManualMatching(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            installments = driver.find_element(By.XPATH, "//span[text()='Reconciliation']/parent::a")

            if "active-menuitem" in installments.get_attribute("class"):
                logging.info("Successfully clicked the Reconciliation icon ")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/a/i[2]")
                click_icon.click()
                logging.info("Successfully clicked the Reconciliation icon ")

            time.sleep(2)

            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[6]/adad-frontend-sidebar-item/ul/li[5]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Manual Maching item!")
            time.sleep(2)

            assert "manual-matching" in driver.current_url, "❌ Not on Manual Maching page"
            logging.info("-------Successfully Navigated to Manual Maching page------")
        # Assign metadata separately
        tp_id = "TP0013"
        tp_description = f"Navigate to Manual Maching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  