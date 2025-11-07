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

######################################################################################################################################
######################################################################################################################################
###############################                       ################################################################################
###############################   Quick filters Sales #########################################################################
###############################                       ################################################################################
######################################################################################################################################
######################################################################################################################################


class ManualMatchingUIFilterSelectPNROrderREferenceToFilter(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            time.sleep(1)
           
            try:
                # Wait until input is visible and interactable
                icon_ckeck_click = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-sales-list/div/div/div/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[1]/div[3]/p-radiobutton/div/div[2]"))
                )
                
                # Clear any existing text before typing
                icon_ckeck_click.click()
               
                logging.info(f"✅ PNR/Order Reference icon check clicked")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click PNR/Order Reference icon")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click PNR/Order Reference icon in manual matching view"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingSaleUIFilterPNROrderReference(TestPoint):
    def __init__(self, pnr_order_reference ):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            time.sleep(1)
            
            try:
                # Wait until input is visible and interactable
                sale_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-sales-list/div/div/div/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/input"))
                )
                
                # Clear any existing text before typing
                sale_id_input.clear()
                sale_id_input.send_keys(pnr_order_reference)
                logging.info(f"✅ PNR order reference'{pnr_order_reference}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter PNR")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter PNR Order Reference"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  









class ManualMatchingUISaleClickSearchQuickFilters(TestPoint):
    def __init__(self):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try:
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.p-0:nth-child(2) > div:nth-child(1) > adad-frontend-quick-search-standalone-filter:nth-child(1) > div:nth-child(1) > p-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(2)"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Search' button clicked successfully")

                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click the 'Search' button")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP1415"
        tp_description = f"click the sale 'Search' button in manual matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  






















######################################################################################################################################
######################################################################################################################################
###############################                             #########################################################################
###############################   Quick filters Settlements #########################################################################
###############################                             #########################################################################
######################################################################################################################################
######################################################################################################################################


class ManualMatchingUISettlementFilterSelectPNROrderReferenceToFilter(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            time.sleep(1)
           
            try:
                # Wait until input is visible and interactable
                icon_ckeck_click = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-settlements-list/div/div/div/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[1]/div[3]/p-radiobutton/div/div[2]"))
                )
                
                # Clear any existing text before typing
                icon_ckeck_click.click()
               
                logging.info(f"✅ PNR/Order Reference icon check clicked")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click PNR/Order Reference icon")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click PNR/Order Reference icon in manual matching view settlement"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingSettlementUIFilterPNROrderReference(TestPoint):
    def __init__(self, pnr_order_reference ):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            time.sleep(1)
            
            try:
                # Wait until input is visible and interactable
                sale_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-settlements-list/div/div/div/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/input"))
                )
                
                # Clear any existing text before typing
                sale_id_input.clear()
                sale_id_input.send_keys(pnr_order_reference)
                logging.info(f"✅ PNR order reference'{pnr_order_reference}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter PNR in settlement")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter PNR Order Reference settlement"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  







class ManualMatchingUISettlmeentClickSearchQuickFilters(TestPoint):
    def __init__(self):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try:
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "adad-frontend-quick-search-standalone-filter.pl-0 > div:nth-child(1) > p-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(2)"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Search' button clicked successfully")

                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click the 'Search' button")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP1415"
        tp_description = f"click the settlement 'Search' button in manual matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  










class ManualMatchingUISaleFilterPaymentDateRange(TestPoint):
    def __init__(self, date ):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                date_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-sales-list/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
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
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-sales-list/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
                )

                # Send date
                date_input.send_keys(date)
                logging.info(f"✅ Date '{date}' entered")

                # Press Enter
                date_input.send_keys(Keys.ENTER)
                logging.info("✅ ENTER pressed to confirm date")

                time.sleep(2)

            except Exception as e :
                logging.error(e)
                raise AssertionError("❌ Failed to filter payment day")

        # Assign metadata separately
        tp_id = "TP1400"
        tp_description = f"Filter payment date range in pending sales within manual matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterChannelType(TestPoint):
    def __init__(self, channel_type):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try:
                # Wait for dropdown trigger and click it
                dropdown_trigger = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-sales-list/div/div/div[2]/adad-frontend-sale-sources-dropdown-filter/div/p-dropdown"))
                )
                dropdown_trigger.click()
                logging.info("✅ Dropdown opened")
                time.sleep(1)

                # Wait for the option list and click the desired option
                option = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][normalize-space()='{channel_type}']"))
                )

                option.click()
                logging.info(f"✅ Option '{channel_type}' selected")

                time.sleep(1)

                # Verify the selected value
                selected_label = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "span.p-dropdown-label"))
                )
                logging.info(f"🎯 Dropdown now shows: '{selected_label.text}'")

            except Exception as e:
                logging.error(e)
                logging.exception("❌ Failed to select channel type")
                raise AssertionError("❌")

        # Assign metadata separately
        tp_id = "TP1401"
        tp_description = f"Filter channel type in pending sales within manual matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterCountry(TestPoint):
    def __init__(self, channel_type = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌")

        # Assign metadata separately
        tp_id = "TP1402"
        tp_description = f"Filter country in pending sales within manual matching page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterDocumentNumber(TestPoint):
    def __init__(self, document_number):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try:
                # Wait until the input is visible and clickable
                document_number_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-sales-list/div/div/div[4]/input")
                    )
                )

                # Clear any existing text
                document_number_input.clear()

                # Send the document number
                document_number_input.send_keys(document_number)
                logging.info(f"✅ Document number '{document_number}' entered successfully")

                time.sleep(2)

            except Exception as e:
                logging.error("❌ Failed to enter document number")
                raise AssertionError("❌")

        # Assign metadata separately
        tp_id = "TP1404"
        tp_description = f"Filter document number in pending sales within manual matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleAddFilters(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌")

        # Assign metadata separately
        tp_id = "TP1405"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterSaleID(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1406"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterFileID(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1407"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterFileFOPCode(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1408"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterFileFOPSubCode(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1409"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterPaymentID(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1410"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterPaymentCurrency(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1411"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterCCBin(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1412"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterCC4LastDigits(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1413"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleFilterApprovalCode(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1414"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleClickSearch(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try:
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.p-fluid:nth-child(2) > div:nth-child(6) > div:nth-child(2) > button:nth-child(1) > span:nth-child(1)"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Search' button clicked successfully")

                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click the 'Search' button")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP1415"
        tp_description = f"click the sale 'Search' button"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  


class ManualMatchingUISettlementFilterPaymentDateRange(TestPoint):
    def __init__(self, date ):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            date_input = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-settlements-list/div/div[1]/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input").click()
            time.sleep(2)
            clear= driver.find_element(By.XPATH, "/html/body/div/div[2]/button[2]/span").click()
            time.sleep(2)
            date_input = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-settlements-list/div/div[1]/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input")
            date_input.send_keys(date)
            date_input.send_keys(Keys.ENTER)
            time.sleep(2)

        # Assign metadata separately
        tp_id = "TP1416"
        tp_description = f"Filter payment date range in pending Settlements within manual matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterCustomerAcquirer(TestPoint):
    def __init__(self, customer):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                dropdown_trigger = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-settlements-list/div/div/div/div[2]/adad-frontend-acquirers-dropdown-filter/div/p-dropdown/div")))
                dropdown_trigger.click()
                logging.info("✅ Dropdown opened")
                time.sleep(1)
                option = driver.find_element(By.XPATH, f"//ul[@role='listbox']//li[@role='option'][normalize-space()='{customer}']/span").click()
                logging.info(f"✅ Option '{option}' selected")

                time.sleep(1)

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1417"
        tp_description = f"Filter channel type in pending Settlements within manual matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterCountry(TestPoint):
    def __init__(self, channel_type = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1402"
        tp_description = f"Filter country in pending Settlements within manual matching page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterDocumentNumber(TestPoint):
    def __init__(self, document_number ):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                document_number_input = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-settlements-list/div/div/div/div[5]/input").send_keys(document_number)
                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1404"
        tp_description = f"Filter document number in pending Settlements within manual matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementAddFilters(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ ")

        # Assign metadata separately
        tp_id = "TP1405"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterSettlementID(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ ")

        # Assign metadata separately
        tp_id = "TP1406"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterFileID(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1407"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterFileFOPCode(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1408"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterFileFOPSubCode(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1409"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterPaymentID(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1410"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterPaymentCurrency(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)

        # Assign metadata separately
        tp_id = "TP1411"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterCCBin(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ ")

        # Assign metadata separately
        tp_id = "TP1412"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterCC4LastDigits(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ ")

        # Assign metadata separately
        tp_id = "TP1413"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementFilterApprovalCode(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ ")

        # Assign metadata separately
        tp_id = "TP1414"
        tp_description = f""
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementClickSearch(TestPoint):
    def __init__(self, document_number = str):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.p-fluid:nth-child(1) > div:nth-child(6) > div:nth-child(2) > button:nth-child(1)"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Search' button clicked successfully")

                time.sleep(2)

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ 'Search' button clicking failed")

        # Assign metadata separately
        tp_id = "TP1415"
        tp_description = f"click the settlement 'Search' button"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISaleClickCheckBox(TestPoint):
    def __init__(self,):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-sales-list/div/adad-frontend-table/p-table/div/div[2]/table/tbody/tr/td[1]/p-tablecheckbox/div/div[2]"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Checkbox' clicked successfully")

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ 'Checkbox' clicking failed ")

        # Assign metadata separately
        tp_id = "TP1416"
        tp_description = f"click the sale checkbox "
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUISettlementClickCheckBox(TestPoint):
    def __init__(self,):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-settlements-list/div/adad-frontend-table/p-table/div/div[2]/table/tbody/tr/td[1]/p-tablecheckbox/div/div[2]"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Checkbox' clicked successfully")

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ 'Checkbox' clicking failed ")

        # Assign metadata separately
        tp_id = "TP1417"
        tp_description = f"click the settlement checkbox "
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUIConfirmMatching(TestPoint):
    def __init__(self,):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/div/div/adad-frontend-manual-matching-of-sales-and-settlements/div/adad-frontend-manual-matching-selection-summary/div/div/div[6]/button[1]"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Confirm' clicked successfully")

                time.sleep(2)


            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ 'Confirm' clicking failed")

        # Assign metadata separately
        tp_id = "TP1418"
        tp_description = f"click the confirmation "
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUIMatchSaleAndSettlement(TestPoint):
    def __init__(self,):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/adad-frontend-manual-matching-of-sales-and-settlements-confirm-dialog/div/div[2]/button"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Match Sale And Settlement' clicked successfully")

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌ Match Sale And Settlement clicking failed")

        # Assign metadata separately
        tp_id = "TP1419"
        tp_description = f"click the Match Sale And Settlement "
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class ManualMatchingUIMatchSaleAndSettlementClickYes(TestPoint):
    def __init__(self,):   
        def func(driver ):
            assert "/manual-matching" in driver.current_url, "❌ Not on manual matching page"
            try : 
                # Wait until the Search button is clickable
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-manual-matching/adad-frontend-confirm-dialog/p-confirmdialog/div/div/div[3]/button[2]"))
                )

                # Click the button
                search_button.click()
                logging.info("✅ 'Match Sale And Settlement Yes' clicked successfully")

                time.sleep(2)

            except Exception as e :
                logging.exception(e)
                raise AssertionError("❌Match Sale And Settlement Yes' clicking failed")

        # Assign metadata separately
        tp_id = "TP1420"
        tp_description = f"click the Match Sale And Settlement yes"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  








