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

class FileDashboardUIFilterExpectedFileReceptionDate(TestPoint):
    def __init__(self):   
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            date_input = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-files-list/div/div/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input").click()
            time.sleep(2)
            clear= driver.find_element(By.XPATH, "/html/body/div/div[2]/button[2]").click()
            time.sleep(2)
            date_input = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-files-list/div/div/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input")
            date_input.send_keys(date)
            date_input.send_keys(Keys.ENTER)
            time.sleep(2)

        # Assign metadata separately
        tp_id = "TP0500"
        tp_description = f"Filter expected file reception date within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class FileDashboardUIFilterFileReceptionDate(TestPoint):

    def __init__(self):  
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            date_input = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-files-list/div/div/div/div/div[2]/adad-frontend-date-range/div/div/p-calendar/span/input").click()
            time.sleep(2)
            clear= driver.find_element(By.XPATH, "/html/body/div/div[2]/button[2]/span").click()
            time.sleep(2)
            date_input = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-files-list/div/div/div/div/div[2]/adad-frontend-date-range/div/div/p-calendar/span/input")
            date_input.send_keys(date)
            date_input.send_keys(Keys.ENTER)
            time.sleep(2)

        # Assign metadata separately
        tp_id = "TP0501"
        tp_description = f"Filtersfile reception date within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class FileDashboardUIAddFilters(TestPoint):  

    def __init__(self):   
        
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            time.sleep(2)
            filters = driver.find_element(By.CSS_SELECTOR, "button.field")
            time.sleep(2)
            if filters.get_attribute("class") == "p-element field p-button p-component p-button-icon-only" :
                logging.info("Successfully clicked the add filters icon *")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR ,"button.field")
                click_icon.click()
                logging.info("Successfully clicked the add filters icon **")
            time.sleep(2)


        # Assign metadata separately
        tp_id = "TP0502"
        tp_description = f"Add other ui filters within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")     

class FileDashboardUIFilterFileID(TestPoint):  

    def __init__(self, file_id ):   
        
        def func(driver = webdriver):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            time.sleep(2)
            try :
                FileDashboardUIAddFilters().run(driver)
                filters = driver.find_element(By.CSS_SELECTOR, "input.p-inputtext:nth-child(2)")
                filters.send_keys(file_id)
                filters.send_keys(Keys.ENTER)
            except Exception as e:
                logging.exception(e)
            time.sleep(2)


        # Assign metadata separately
        tp_id = "TP0503"
        tp_description = f"Filter File ID within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")     

class FileDashboardUIFilterFileStatus(TestPoint):  

    def __init__(self):  
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            


        # Assign metadata separately
        tp_id = "TP0504"
        tp_description = f"Filter file status within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class FileDashboardUIFilterDataSourceType(TestPoint):  

    def __init__(self):  
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            


        # Assign metadata separately
        tp_id = "TP0505"
        tp_description = f"Filter Data source type within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")    

class FileDashboardUIFilterDataSource(TestPoint):  

    def __init__(self):   
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            


        # Assign metadata separately
        tp_id = "TP0506"
        tp_description = f"Filter data source within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class FileDashboardUIFilterDefaultMarket(TestPoint):  

    def __init__(self):   
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            


        # Assign metadata separately
        tp_id = "TP0507"
        tp_description = f"Filter default market within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class FileDashboardUIFilterClickSearch(TestPoint):  

    def __init__(self):   
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            time.sleep(2)
            try :
                filters = driver.find_element(By.CSS_SELECTOR, "div.mt-4 > button:nth-child(1)").click()

            except Exception as e :
                logging.exception(e)
            time.sleep(2)

        # Assign metadata separately
        tp_id = "TP0508"
        tp_description = f"Click search within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class FileDashboardUILoadMore(TestPoint):  

    def __init__(self):   
        def func(driver = webdriver, date = str):
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            


        # Assign metadata separately
        tp_id = "TP0509"
        tp_description = f"Click load more within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class CheckIfFileIngested(TestPoint):  

    def __init__(self, file_name ):  
        def func(driver = webdriver):
            time.sleep(3)
            assert "/etl-files" in driver.current_url, "❌ Not on file dashboard page"
            tbody = driver.find_element(By.CSS_SELECTOR, "tbody.p-datatable-tbody")
            rows = driver.find_elements(By.CSS_SELECTOR, "tbody.p-datatable-tbody tr")

            # Debug print to see what’s captured
            first_row_text = rows[0].text.strip()
            logging.info(f"Found {len(rows)} rows")
            check = False 
            if "No data" in first_row_text:
                
                logging.error("❌ Table is empty (No data row found)")
                raise AssertionError("❌ Table is empty (No data)")
            else :
                for i in range(0,len(rows)) :
                    first_row_text = rows[i].text.strip()
                    list_of_file = first_row_text.split('\n')
                    if file_name == list_of_file[2] :
                        check =True
                        logging.info("✅ File injected found in list of files")
                    logging.info(list_of_file)

            # Assert that there is at least one row
            assert len(rows) > 0, "❌ Table is empty, but it should not be!"
            assert check, "❌ File not found, but it should not be!"


        # Assign metadata separately
        tp_id = "TP0510"
        tp_description = f"Check if file ingested within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  