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

class SettlementUISelectSettlementOrPaymentOrder(TestPoint):
    def __init__(self, label="Settlement" ):   
        def func(driver ):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit-track/Settlement page"
            
            try:
                # Locate the option by its aria-label
                option = driver.find_element(By.XPATH, f"//div[@role='button' and @aria-label='{label}']")
                
                # Check if already selected
                if option.get_attribute("aria-pressed") == "true":
                    logging.info(f"⚠️ '{label}' already selected, skipping click")
                else:
                    option.click()
                    logging.info(f"✅ '{label}' selected successfully")
            except Exception as e:
                logging.exception(f"❌ Failed to select '{label}'")
                raise

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Select settlement or payment order within Settlement page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  




class SettlementUIFilterPaymentDateRange(TestPoint):
    def __init__(self, date ):   
        def func(driver ):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit-track/Settlement page"
            SettlementUISelectSettlementOrPaymentOrder().func(driver)
            date_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-settlements-audit-track/div/adad-frontend-settlements-audit-track-filters/div/div[1]/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
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
                EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-settlements-audit-track/div/adad-frontend-settlements-audit-track-filters/div/div[1]/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
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
        tp_description = f"Filter payment date range in Settlements within Settlement page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIFilterCustomerAcquirer(TestPoint):
    def __init__(self, channel_type ):   
        def func(driver = webdriver):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit-track/Settlement page"
            SettlementUISelectSettlementOrPaymentOrder().func(driver)
            try :
                channel_type_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-settlements-audit-track/div/adad-frontend-settlements-audit-track-filters/div/div/div/div[2]/adad-frontend-acquirers-dropdown-filter/div/p-dropdown/div"))
    )
                channel_type_input.click()
                logging.info("✅ customer/acquirer clicked")

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
                logging.exception("❌ Failed to select customer/acquirer")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter customer/acquirer in Settlements within Settlement page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIFilterCountry(TestPoint):
    def __init__(self, country ):   
        def func(driver = webdriver):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit-track/Settlement page"
            SettlementUISelectSettlementOrPaymentOrder().func(driver)
            try :
                


                time.sleep(2)
            except Exception as e: 
                logging.exception("❌ Failed to filter country")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter filter in Settlements within Settlement page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIFilterPNROrderReference(TestPoint):
    def __init__(self, pnr ):   
        def func(driver ):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit-track/Settlement page"
            SettlementUISelectSettlementOrPaymentOrder().func(driver)
            try :
                pnr_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-settlements-audit-track/div/adad-frontend-settlements-audit-track-filters/div/div/div/div[4]/input"))
    )
                pnr_input.send_keys(pnr)
                logging.info("✅ pnr value {pnr} clicked")

                time.sleep(2)
                
            except Exception as e: 
                logging.exception("❌ Failed to filter customer/acquirer")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter customer/acquirer in Settlements within Settlement page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIAddFilters(TestPoint):
    def __init__(self ):   
        def func(driver = webdriver):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track Settlement page"
            SettlementUISelectSettlementOrPaymentOrder().func(driver)
            time.sleep(1)
            try:
                # Try to detect if panel is open
                try:
                    panel = driver.find_element(By.XPATH, "//div[contains(@class,'filter-panel')]")
                    if panel.is_displayed():
                        logging.info("⚠️ Filter panel already open, skipping click...")
                        return
                except:
                    logging.info("ℹ️ Filter panel not open, will click button")

                # Click the button only if panel is not open
                button = driver.find_element(By.XPATH, "//button[@icon='pi pi-filter']")
                button.click()
                logging.info("✅ Filter button clicked")


            except Exception as e:
                logging.exception("❌ Failed to add filters")
                raise AssertionError(e) 
        

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIFilterSettlementID(TestPoint):
    def __init__(self, Settlement_id ):   
        def func(driver = webdriver):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track Settlement page"
            SettlementUISelectSettlementOrPaymentOrder().func(driver)
            time.sleep(1)
            SettlementUIAddFilters().run(driver)
            try:
                # Wait until input is visible and interactable
                Settlement_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-settlements-audit-track/div/adad-frontend-settlements-audit-track-filters/div/div[2]/div/div[1]/div[1]/input"))
                )
                
                # Clear any existing text before typing
                Settlement_id_input.clear()
                Settlement_id_input.send_keys(Settlement_id)
                logging.info(f"✅ Settlement ID '{Settlement_id}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter PNR")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIClickSearch(TestPoint):
    def __init__(self ):   
        def func(driver = webdriver):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track Settlement page"
            SettlementUISelectSettlementOrPaymentOrder().func(driver)
            try :
                time.sleep(1)
                filters = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-settlements-audit-track/div/adad-frontend-settlements-audit-track-filters/div/div/div/div[6]/div/button").click()
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
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUICheckIfFileFound(TestPoint):  

    def __init__(self):  
        def func(driver = webdriver, file_id = str):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track Settlement page"
            SettlementUISelectSettlementOrPaymentOrder().func(driver)
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
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  


class SettlementUIPaymentOrderFilterPaymentDateRange(TestPoint):
    def __init__(self, date ):   
        def func(driver ):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit-track/Settlement page"
            SettlementUISelectSettlementOrPaymentOrder("Payment Order").func(driver)
            date_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-payment-orders-audit-track/div/div[1]/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
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
                EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-payment-orders-audit-track/div/div[1]/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
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
        tp_description = f"Filter payment date range in payment order within Settlement payment order page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIPaymentOrderFilterCustomerAcquirer(TestPoint):
    def __init__(self, channel_type ):   
        def func(driver = webdriver):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit-track/Settlement page"
            SettlementUISelectSettlementOrPaymentOrder("Payment Order").func(driver)
            try :
                channel_type_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-payment-orders-audit-track/div/div[1]/div/div/div[2]/adad-frontend-acquirers-dropdown-filter/div/p-dropdown/div"))
    )
                channel_type_input.click()
                logging.info("✅ customer/acquirer clicked")

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
                logging.exception("❌ Failed to select customer/acquirer")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter customer/acquirer in Settlements within Settlement page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIPaymentOrderFilterPaymentOrderID(TestPoint):
    def __init__(self, Settlement_id ):   
        def func(driver = webdriver):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track Settlement page"
            SettlementUISelectSettlementOrPaymentOrder("Payment Order").func(driver)
            time.sleep(1)
            SettlementUIAddFilters().run(driver)
            try:
                # Wait until input is visible and interactable
                Settlement_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-settlements-audit-track/div/adad-frontend-settlements-audit-track-filters/div/div[2]/div/div[1]/div[1]/input"))
                )
                
                # Clear any existing text before typing
                Settlement_id_input.clear()
                Settlement_id_input.send_keys(Settlement_id)
                logging.info(f"✅ Settlement ID '{Settlement_id}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter PNR")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIPaymentOrderClickSearch(TestPoint):
    def __init__(self ):   
        def func(driver = webdriver):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track Settlement page"
            SettlementUISelectSettlementOrPaymentOrder("Payment Order").func(driver)
            try :
                time.sleep(1)
                filters = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-settlement-audit-track-view/div/adad-frontend-payment-orders-audit-track/div/div[1]/div/div/div[6]/button").click()
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
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SettlementUIPaymentOrderCheckIfFileFound(TestPoint):  

    def __init__(self):  
        def func(driver = webdriver, file_id = str):
            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track Settlement page"
            SettlementUISelectSettlementOrPaymentOrder("Payment Order").func(driver)
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
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  







