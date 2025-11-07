import pytest
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
###############################   Quick filters       ################################################################################
###############################                       ################################################################################
######################################################################################################################################
######################################################################################################################################

class SaleUIFilterSelectSaleIDToFilter(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
           
            try:
                # Wait until input is visible and interactable
                document_number_icon_ckeck_click = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[1]/div[1]/p-radiobutton/div/div[2]"))
                )
                
                # Clear any existing text before typing
                document_number_icon_ckeck_click.click()
               
                logging.info(f"✅ Sale Id icon check clicked")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click Sale Id icon")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click Sale Id icon"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterSaleID(TestPoint):
    def __init__(self, sale_id ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            try:
                # Wait until input is visible and interactable
                sale_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/input"))
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

class SaleUIFilterSelectDocumentNumberToFilter(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
           
            try:
                # Wait until input is visible and interactable
                document_number_icon_ckeck_click = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[1]/div[2]/p-radiobutton/div/div[2]"))
                )
                
                # Clear any existing text before typing
                document_number_icon_ckeck_click.click()
               
                logging.info(f"✅ document number icon check clicked")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click document number icon")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click document number icon"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterDocumentNumber(TestPoint):
    def __init__(self, document_number ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            SaleUIFilterSelectDocumentNumberToFilter().run(driver)
            try:
                # Wait until input is visible and interactable
                sale_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/input"))
                )
                
                # Clear any existing text before typing
                sale_id_input.clear()
                sale_id_input.send_keys(document_number)
                logging.info(f"✅ Sale ID '{document_number}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter PNR")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"filter document number {document_number}"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterSelectPNROrderReferenceToFilter(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
           
            try:
                # Wait until input is visible and interactable
                pnr_order_reference_icon_ckeck_click = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[1]/div[3]/p-radiobutton"))
                )
                
                # Clear any existing text before typing
                pnr_order_reference_icon_ckeck_click.click()
               
                logging.info(f"✅ PNR/Order Reference icon check clicked")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click PNR/Order Reference icon")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click PNR/Order Reference icon"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterPNROrderReference(TestPoint):
    def __init__(self, pnr_order_reference ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            SaleUIFilterSelectPNROrderReferenceToFilter().run(driver)
            try:
                # Wait until input is visible and interactable
                pnr_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/input"))
                )
                
                # Clear any existing text before typing
                pnr_input.clear()
                pnr_input.send_keys(pnr_order_reference)
                logging.info(f"✅ pnr order reference '{pnr_order_reference}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter PNR")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"filter  pnr order reference {pnr_order_reference}"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterSelectPaymentIDToFilter(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
           
            try:
                # Wait until input is visible and interactable
                payment_id_icon_ckeck_click = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[1]/div[4]/p-radiobutton/div"))
                )
                
                # Clear any existing text before typing
                payment_id_icon_ckeck_click.click()
               
                logging.info(f"✅ Payment ID icon check clicked")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click Payment ID icon")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click Payment ID icon"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterPaymentID(TestPoint):
    def __init__(self, payment_id ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            SaleUIFilterSelectPaymentIDToFilter().run(driver)
            try:
                # Wait until input is visible and interactable
                payment_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/input"))
                )
                
                # Clear any existing text before typing
                payment_id_input.clear()
                payment_id_input.send_keys(payment_id)
                logging.info(f"✅ Payment ID '{payment_id}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter Payment ID")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter Payment ID {payment_id}"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterSelectCreditCardNumberToFilter(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
           
            try:
                # Wait until input is visible and interactable
                credit_card_icon_ckeck = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[1]/div[5]/p-radiobutton"))
                )
                
                # Clear any existing text before typing
                credit_card_icon_ckeck.click()
               
                logging.info(f"✅ Credit Card Number icon check clicked")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click Credit Card Number icon")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click Credit Card Number icon"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

# execution of selection should be befor it
class SaleUIFilterCreditCardBIN(TestPoint):
    def __init__(self, credit_card_bin ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            
            try:
                # Wait until input is visible and interactable
                credit_card_bin_value = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/div/input[1]"))
                )
                
                # Clear any existing text before typing
                credit_card_bin_value.clear()
                credit_card_bin_value.send_keys(credit_card_bin)
                logging.info(f"✅ Credit Card bin '{credit_card_bin}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter Credit Card bin ")
                raise AssertionError(e)
            
        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter Credit Card bin {credit_card_bin}"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

# execution of selection should be befor it
class SaleUIFilterCreditCard4LastDegits(TestPoint):
    def __init__(self, credit_card_4_last_degits ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            try:
                # Wait until input is visible and interactable
                credit_card_4_last_degits_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/div/input[2]"))
                )
                
                # Clear any existing text before typing
                credit_card_4_last_degits_input.clear()
                credit_card_4_last_degits_input.send_keys(credit_card_4_last_degits)
                logging.info(f"✅ Credit Card 4 last degits '{credit_card_4_last_degits}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter Credit Card 4 last degits")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter Credit Card 4 last degits {credit_card_4_last_degits}"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterSelectApprovalCodeToFilter(TestPoint):
    def __init__(self ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
           
            try:
                # Wait until input is visible and interactable
                approval_code_icon_ckeck_click = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[1]/div[6]/p-radiobutton/div"))
                )
                
                # Clear any existing text before typing
                approval_code_icon_ckeck_click.click()
               
                logging.info(f"✅ Approval Code icon check clicked")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to click Approval Code icon")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click Approval Code icon"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterApprovalCode(TestPoint):
    def __init__(self, approval_code ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            SaleUIFilterSelectApprovalCodeToFilter().run(driver)
            try:
                # Wait until input is visible and interactable
                approval_code_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/input"))
                )
                
                # Clear any existing text before typing
                approval_code_input.clear()
                approval_code_input.send_keys(approval_code)
                logging.info(f"✅ Approval Code '{approval_code}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter Approval Code {approval_code}")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter Approval Code {approval_code}"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIClickSearchQuickFilter(TestPoint):
    def __init__(self ):   
        def func(driver = webdriver):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            try :
                time.sleep(1)
                filters = driver.find_element(By.CSS_SELECTOR, ".p-button-primary > span:nth-child(1)").click()
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

class SaleUICheckIfSearchQuickFilterIsClickable(TestPoint):
    def __init__(self, status =True ):   
        def func(driver = webdriver):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            try :
                time.sleep(1)
                search_button = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/button")
                time.sleep(1)
                logging.info("✅Successfully find the search button")

            except Exception as e :
                logging.info("❌ Failed to find search button")
                if status == True:   
                    logging.error("❌ Failed to find search button")             
                    raise AssertionError(e)   
                else :
                    logging.info("✅ Failed to find search button")


        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Check if quick filters search button"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

######################################################################################################################################
######################################################################################################################################
###############################                       ################################################################################
###############################   Advanced filters    ################################################################################
###############################                       ################################################################################
######################################################################################################################################
######################################################################################################################################


class SaleUIFilterPaymentDateRange(TestPoint):
    def __init__(self, date ):   
        def func(driver):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit-track/sale page"
            try : 
                date_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[2]/p-card/div/div[2]/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
    )
                date_input.click()
                logging.info("✅ Date input clicked")
            except Exception  as e :
                pytest.fail("❌ Button not clicked")
                logging.error(e)

            time.sleep(2)

            try : 
            # Wait for clear button and click it
                clear_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/button[2]"))
                )
                clear_btn.click()
                logging.info("✅ Clear button clicked")
            except Exception as e :
                pytest.fail("❌ Button not clicked")
                logging.error(e)
                

            # Check if clear_btn is active
            if clear_btn == driver.switch_to.active_element:
                logging.info("✅ Clear button is now focused")
            else:
                logging.warning("⚠️ Clear button did not get focus")

            time.sleep(2)

            # Re-locate the date input after clearing
            date_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[2]/p-card/div/div[2]/div/div/div[1]/adad-frontend-date-range/div/div/p-calendar/span/input"))
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
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit-track/sale page"
            try :
                channel_type_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[2]/p-card/div/div[2]/div/div/div[2]/adad-frontend-sale-sources-dropdown-filter/div/p-dropdown/div/span"))
    )
                channel_type_input.click()
                logging.info("✅ channel type clicked")

                time.sleep(2)
            except Exception as e: 
                logging.exception("❌ Failed to click select channel type")
                pytest.fail("❌ Failed to click select channel type")

                raise AssertionError(e)
            # Wait for clear button and click it
            
            try:
                option = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][normalize-space()='{channel_type}']"))
                    )
                option.click()
                logging.info(f"✅ Option '{channel_type}' selected")
            except Exception as e: 
                logging.exception("❌ channel type doesn't exist")
                pytest.fail("❌ channel type doesn't exist")

            try :

                selected_label = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "p-dropdown.p-element"))
                    )
                logging.info(f"🎯 Dropdown now shows: '{selected_label.text}'")

            except Exception as e :
                logging.error(e)
            time.sleep(2)
           

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter Channel Type in sales within sale page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterCountry(TestPoint):
    def __init__(self, country ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            try:
                # Wait until input is visible and interactable
                sale_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[2]/p-card/div/div[2]/div/div/div[3]/input"))
                )
                
                # Clear any existing text before typing
                sale_id_input.clear()
                sale_id_input.send_keys(country)
                logging.info(f"✅ Country '{country}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter country")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter country"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterFileID(TestPoint):
    def __init__(self, file_id ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            time.sleep(1)
            try:
                # Wait until input is visible and interactable
                sale_id_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[1]/adad-frontend-quick-search-standalone-filter/div/p-card/div/div[2]/div/div/div[2]/div/input"))
                )
                
                # Clear any existing text before typing
                sale_id_input.clear()
                sale_id_input.send_keys(file_id)
                logging.info(f"✅ File ID '{file_id}' entered successfully")
                
                time.sleep(2)

            except Exception as e:
                logging.exception("❌ Failed to enter File ID")
                raise AssertionError(e)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"filter File ID"
        tkt_id= f"*****"
        tp_status=f"not ready"

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
        tp_description = f"Click add filter"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterFOPCode(TestPoint):
    def __init__(self, fop_code ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit-track/sale page"
            try :
                channel_type_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[2]/p-card/div/div[2]/div/div/div[2]/adad-frontend-sale-sources-dropdown-filter/div/p-dropdown/div/span"))
    )
                channel_type_input.click()
                logging.info("✅ channel type clicked")

                time.sleep(2)
            except Exception as e: 
                logging.exception("❌ Failed to click select channel type")
                pytest.fail("❌ Failed to click select channel type")

                raise AssertionError(e)
            # Wait for clear button and click it
            
            try:
                option = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][normalize-space()='{fop_code}']"))
                    )
                option.click()
                logging.info(f"✅ Option '{fop_code}' selected")
            except Exception as e: 
                logging.exception("❌ channel type doesn't exist")
                pytest.fail("❌ channel type doesn't exist")

            try :

                selected_label = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "p-dropdown.p-element"))
                    )
                logging.info(f"🎯 Dropdown now shows: '{selected_label.text}'")

            except Exception as e :
                logging.error(e)
            time.sleep(2)
           

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter fop code in sales within sale page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterFOPSubCode(TestPoint):
    def __init__(self, fop_code ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit-track/sale page"
            try :
                channel_type_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[2]/p-card/div/div[2]/div/div/div[2]/adad-frontend-sale-sources-dropdown-filter/div/p-dropdown/div/span"))
    )
                channel_type_input.click()
                logging.info("✅ channel type clicked")

                time.sleep(2)
            except Exception as e: 
                logging.exception("❌ Failed to click select channel type")
                pytest.fail("❌ Failed to click select channel type")

                raise AssertionError(e)
            # Wait for clear button and click it
            
            try:
                option = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][normalize-space()='{fop_code}']"))
                    )
                option.click()
                logging.info(f"✅ Option '{fop_code}' selected")
            except Exception as e: 
                logging.exception("❌ channel type doesn't exist")
                pytest.fail("❌ channel type doesn't exist")

            try :

                selected_label = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "p-dropdown.p-element"))
                    )
                logging.info(f"🎯 Dropdown now shows: '{selected_label.text}'")

            except Exception as e :
                logging.error(e)
            time.sleep(2)
           

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter fop code in sales within sale page"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUIFilterSettledStatus(TestPoint):
    def __init__(self, fop_code ):   
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit-track/sale page"
            try :
                channel_type_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-toolbar/div/div/div/div/adad-frontend-sale-audit-track-view/adad-frontend-sales-audit-track/div/adad-frontend-sales-audit-track-filters/div/div[2]/p-card/div/div[2]/div/div/div[2]/adad-frontend-sale-sources-dropdown-filter/div/p-dropdown/div/span"))
    )
                channel_type_input.click()
                logging.info("✅ channel type clicked")

                time.sleep(2)
            except Exception as e: 
                logging.exception("❌ Failed to click select channel type")
                pytest.fail("❌ Failed to click select channel type")

                raise AssertionError(e)
            # Wait for clear button and click it
            
            try:
                option = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][normalize-space()='{fop_code}']"))
                    )
                option.click()
                logging.info(f"✅ Option '{fop_code}' selected")
            except Exception as e: 
                logging.exception("❌ channel type doesn't exist")
                pytest.fail("❌ channel type doesn't exist")

            try :

                selected_label = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "p-dropdown.p-element"))
                    )
                logging.info(f"🎯 Dropdown now shows: '{selected_label.text}'")

            except Exception as e :
                logging.error(e)
            time.sleep(2)
           

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Filter fop code in sales within sale page"
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
                filters = driver.find_element(By.CSS_SELECTOR, ".p-button-primary > span:nth-child(1)").click()
                time.sleep(1)
                logging.info("✅Successfully clicked the search button")

            except Exception as e :
                logging.exception("❌ Failed to click search button")
                raise AssertionError(e)         
            
            time.sleep(2)

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"click search button"
        tkt_id= f"*****"
        tp_status=f"ready"

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


class SaleUICheckIfSaleTableNotEmpty(TestPoint):  

    def __init__(self ):  
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            tbody = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "tbody.p-datatable-tbody"))
)
            rows = driver.find_elements(By.CSS_SELECTOR, "tbody.p-datatable-tbody tr")
            logging.info(f"🧩 Found {len(rows)} rows in Sales Audit Track table")
            if not rows:
                logging.error("❌ No rows found in the table at all")
                raise AssertionError("❌ No rows found in the table")

            else:
                check = False
                for idx, row in enumerate(rows):
                    row_text = row.text.strip()
                    cells = row_text.split('\n')
                    logging.info(f"🔹 Row {idx+1}: {cells}")

                    # Ensure there are enough columns before accessing index 2
                    if len(cells) > 2 :
                        check = True
                        logging.info(f"✅ File found in row {idx+1}")
                        break
                if not check:
                    
                    raise AssertionError(f"❌ File not found in table")

            

            logging.info("✅ Table verification completed successfully")

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Check if file matching done correctly"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class SaleUICheckIfSaleTableEmpty(TestPoint):  

    def __init__(self ):  
        def func(driver ):
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            tbody = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "tbody.p-datatable-tbody"))
)
            rows = driver.find_elements(By.CSS_SELECTOR, "tbody.p-datatable-tbody tr")
            logging.info(f"🧩 Found {len(rows)} rows in Sales Audit Track table")
            if not rows:
                logging.info("❌ No rows found in the table at all")
                raise AssertionError("❌ No rows found in the table")

            else:
                check = True
                for idx, row in enumerate(rows):
                    row_text = row.text.strip()
                    cells = row_text.split('\n')
                    logging.info(f"🔹 Row {idx+1}: {cells}")

                    # Ensure there are enough columns before accessing index 2
                    if len(cells) > 2 :
                        check = False
                        logging.info(f"❌ File found in row {idx+1}")
                        break
                if not check:
                    
                    raise AssertionError(f"❌ File found in table")

            

            logging.info("✅ Table verification completed successfully")

        # Assign metadata separately
        tp_id = "TP"
        tp_description = f"Check if file matching done correctly"
        tkt_id= f"*****"
        tp_status=f"not ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  


