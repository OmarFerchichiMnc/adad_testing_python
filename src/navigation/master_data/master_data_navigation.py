from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestPointNavigateToMasterDataRateOfExchange(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            master_data = driver.find_element(By.XPATH, "//span[text()='Master Data']/parent::a")

            if "active-menuitem" in master_data.get_attribute("class"):
                logging.info("Successfully clicked the master data icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the master data icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the rate of exchange item!")
            time.sleep(2)

            assert "/roe" in driver.current_url, "❌ Not on rate of exchange page"
            logging.info("-------Successfully Navigated to rate of exchange page------")
        # Assign metadata separately
        tp_id = "TP0032"
        tp_description = f"Navigate to rate of exchange page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataFxRateSources(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            master_data = driver.find_element(By.XPATH, "//span[text()='Master Data']/parent::a")

            if "active-menuitem" in master_data.get_attribute("class"):
                logging.info("Successfully clicked the master data icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the master data icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the fx rate source item!")
            time.sleep(2)

            assert "/fx-rate-sources" in driver.current_url, "❌ Not on fx rate source page"
            logging.info("-------Successfully Navigated to fx rate source page------")
        # Assign metadata separately
        tp_id = "TP0033"
        tp_description = f"Navigate to fx rate source page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataFormOfPayments(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            master_data = driver.find_element(By.XPATH, "//span[text()='Master Data']/parent::a")

            if "active-menuitem" in master_data.get_attribute("class"):
                logging.info("Successfully clicked the master data icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the master data icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the form of payments item!")
            time.sleep(2)

            assert "/form-of-payments" in driver.current_url, "❌ Not on form of payments page"
            logging.info("-------Successfully Navigated to form of payments page------")
        # Assign metadata separately
        tp_id = "TP0034"
        tp_description = f"Navigate to form of payments page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataPointOfSales(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            master_data = driver.find_element(By.XPATH, "//span[text()='Master Data']/parent::a")

            if "active-menuitem" in master_data.get_attribute("class"):
                logging.info("Successfully clicked the master data icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the master data icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the point of sales item!")
            time.sleep(2)

            assert "/point-of-sales" in driver.current_url, "❌ Not on point of sales page"
            logging.info("-------Successfully Navigated to point of sales page------")
        # Assign metadata separately
        tp_id = "TP0035"
        tp_description = f"Navigate to point of sales page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataPointOfSalesMerchantMapping(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            master_data = driver.find_element(By.XPATH, "//span[text()='Master Data']/parent::a")

            if "active-menuitem" in master_data.get_attribute("class"):
                logging.info("Successfully clicked the master data icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the master data icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/ul/li[5]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the point of sales merchant mapping item!")
            time.sleep(2)

            assert "/point-of-sales-merchant-mapping" in driver.current_url, "❌ Not on point of sales merchant mapping page"
            logging.info("-------Successfully Navigated to point of sales merchant mapping page------")
        # Assign metadata separately
        tp_id = "TP0036"
        tp_description = f"Navigate to point of sales merchant mapping page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataAcquirers(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            master_data = driver.find_element(By.XPATH, "//span[text()='Master Data']/parent::a")

            if "active-menuitem" in master_data.get_attribute("class"):
                logging.info("Successfully clicked the master data icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the master data icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/ul/li[6]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the acquirers item!")
            time.sleep(2)

            assert "/acquirers" in driver.current_url, "❌ Not on acquirers page"
            logging.info("-------Successfully Navigated to acquirers page------")
        # Assign metadata separately
        tp_id = "TP0037"
        tp_description = f"Navigate to acquirers page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataAcquirersMerchants(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            master_data = driver.find_element(By.XPATH, "//span[text()='Master Data']/parent::a")

            if "active-menuitem" in master_data.get_attribute("class"):
                logging.info("Successfully clicked the master data icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the master data icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/ul/li[7]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the acquirers merchants item!")
            time.sleep(2)

            assert "/acquirer-merchants" in driver.current_url, "❌ Not on acquirers merchants page"
            logging.info("-------Successfully Navigated to acquirers merchants page------")
        # Assign metadata separately
        tp_id = "TP0038"
        tp_description = f"Navigate to acquirers merchants page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataSaleSources(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            master_data = driver.find_element(By.XPATH, "//span[text()='Master Data']/parent::a")

            if "active-menuitem" in master_data.get_attribute("class"):
                logging.info("Successfully clicked the master data icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the master data icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[10]/adad-frontend-sidebar-item/ul/li[8]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the sale sources item!")
            time.sleep(2)

            assert "/sale-sources" in driver.current_url, "❌ Not on sale sources page"
            logging.info("-------Successfully Navigated to sale sources page------")
        # Assign metadata separately
        tp_id = "TP0039"
        tp_description = f"Navigate to sale sources page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  