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

class SaleUICheckIfMatchingDoneCorrectly(TestPoint):  

    def __init__(self, file_name ):  
        def func(driver = webdriver):
            assert "/matched-items" in driver.current_url, "❌ Not on matched items sale page"
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
        tp_id = "TP"
        tp_description = f"Check if file matching done correctly"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  


