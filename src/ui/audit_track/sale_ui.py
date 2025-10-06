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

class SaleUIFilterPaymentDateRange(TestPoint):
    def __init__(self, date ):   
        def func(driver = webdriver):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit-track/sale page"
            date_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
)
            date_input.click()
            logging.info("✅ Date input clicked")

            time.sleep(2)

            # Wait for clear button and click it
            clear_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/button[2]"))
            )
            clear_btn.click()
            logging.info("✅ Clear button clicked")

            # Check if clear_btn is active
            if clear_btn == driver.switch_to.active_element:
                logging.info("✅ Clear button is now focused")
            else:
                logging.warning("⚠️ Clear button did not get focus")

            time.sleep(2)

            # Re-locate the date input after clearing
            date_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
            )

            # Send date
            date_input.send_keys(date)
            logging.info(f"✅ Date '{date}' entered")

            # Press Enter
            date_input.send_keys(Keys.ENTER)
            logging.info("✅ ENTER pressed to confirm date")

            time.sleep(2)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter payment date range in sales within sale page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterChannelType(TestPoint):
    def __init__(self, channel_type ):   
        def func(driver = webdriver):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit-track/sale page"
            try :
                channel_type_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div/div/div[2]/adad-frontend-sale-sources-dropdown-filter/div/p-dropdown"))
    )
                channel_type_input.click()
                logging.info("✅ channel type clicked")

                time.sleep(2)

                # Wait for clear button and click it
                
                option = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][normalize-space()='{channel_type}']"))
                    )
                option.click()
                logging.info(f"✅ Option '{channel_type}' selected")

                selected_label = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "p-dropdown.p-element"))
                    )
                logging.info(f"🎯 Dropdown now shows: '{selected_label.text}'")


                time.sleep(2)
            except Exception as e: 
                logging.exception("❌ Failed to select channel type")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter payment date range in sales within sale page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIAddFilters(TestPoint):
    def __init__(self ):   
        def func(driver = webdriver):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
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
        tp_id = "TP"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterSaleID(TestPoint):
    def __init__(self, sale_id ):   
        def func(driver = webdriver):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            SaleUIAddFilters().run(driver)
            try:
                # Wait until input is visible and interactable
                sale_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[2]/div/div[1]/div[1]/input"))
                )
                
                # Clear any existing text before typing
                sale_id_input.clear()
                sale_id_input.send_keys(sale_id)
                logging.info(f"✅ Sale ID '{sale_id}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter PNR")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  


class SaleUIClickSearch(TestPoint):
    def __init__(self ):   
        def func(driver = webdriver):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            try :
                time.sleep(1)
                filters = driver.find_element(By.CSS_SELECTOR, "div.col-12:nth-child(6) > div:nth-child(2) > button:nth-child(1)").click()
                time.sleep(1)
                logging.info("✅Successfully clicked the search button")

            except Exception as e :
                logging.exception("❌ Failed to click search button")
                raise AssertionError(e)         
            
            time.sleep(2)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUICheckIfFileFound(TestPoint):  

    def __init__(self):  
        def func(driver = webdriver, file_id = str):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            tbody = driver.find_element(By.CSS_SELECTOR, "tbody.p-datatable-tbody")
            rows = driver.find_elements(By.CSS_SELECTOR, "tbody.p-datatable-tbody tr")

            # Debug print to see what’s captured
            logging.info(f"Found {len(rows)} rows")
            first_row_text = rows[0].text.strip()
            if "No data" in first_row_text:
                logging.error("❌ Table is empty (No data row found)")
                raise AssertionError("❌ Table is empty (No data)")

            # Assert that there is at least one row
            assert len(rows) > 0, "❌ Table is empty, but it should not be!"


        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Check if file ingested within file dashboard page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  







