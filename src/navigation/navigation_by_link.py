from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException


class TestPointNavigateToAccountingJournalByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/accounting-journal")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/accounting-journal" in driver.current_url, "❌ Not on accounting journal page"
            execution_status = "passed"
            logging.info("-------Successfully Navigated to accounting journal page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0015"
        tp_description = f"Navigate to accounting journal page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToUnaccountedEventsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/unaccounted-events")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")
            

            assert "/unaccounted-events" in driver.current_url, "❌ Not on unaccounting events page"
            
            logging.info("-------Successfully Navigated to unaccounting events page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0016"
        tp_description = f"Navigate to unaccounting events page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToImbalancedJournalEntriesByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/imbalanced-items")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/imbalanced-items" in driver.current_url, "❌ Not on Imbalanced Journal Entries page"
            execution_status = "passed"
            logging.info("-------Successfully Navigated to Imbalanced Journal Entries page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0017"
        tp_description = f"Navigate to Imbalanced Journal Entries page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToTrialBalanceByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/trial-balance")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/trial-balance" in driver.current_url, "❌ Not on trial balance page"
            execution_status = "passed"
            logging.info("-------Successfully Navigated to trial balance page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0018"
        tp_description = f"Navigate to trial balance page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToPostToLedgerByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/post-to-ledger")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/post-to-ledger" in driver.current_url, "❌ Not on post to ledger page"
            execution_status = "passed"
            logging.info("-------Successfully Navigated to post to ledger page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0019"
        tp_description = f"Navigate to post to ledger page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToAlertManagementByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/alerts")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")


            assert "/alerts" in driver.current_url, "❌ Not on alerts management page"
            logging.info("-------Successfully Navigated to alerts management page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0002"
        tp_description = f"Navigate to Alert management page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToReconciliationAlertsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/reconciliation-alerts")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/reconciliation-alerts" in driver.current_url, "❌ Not on reconciliation alerts page"
            logging.info("-------Successfully Navigated to areconciliation alerts page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0003"
        tp_description = f"Navigate to Reconciliation Alert page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToAuditTrackSaleByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/audit-track/sale")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")
            time.sleep(3)
            assert "/audit-track/sale" in driver.current_url, "❌ Not on audit track sale page"
            logging.info("-------Successfully Navigated to audit track sale page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0006"
        tp_description = f"Navigate to audit track sale page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToAuditTrackSettlementByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/audit-track/settlement")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/audit-track/settlement" in driver.current_url, "❌ Not on audit track settlement page"
            logging.info("-------Successfully Navigated to audit track settlement page------")

            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0007"
        tp_description = f"Navigate to audit track settlement page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  


class TestPointNavigateToBusinesssRulesAlertTypeAffiliationByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/alert-type-affiliation")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/alert-type-affiliation" in driver.current_url, "❌ Not on Alert Type Afiliation page"
            logging.info("-------Successfully Navigated to Alert Type Afiliation page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0020"
        tp_description = f"Navigate to Alert Type Afiliation page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesDataIngestionSettingsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/settings")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/settings" in driver.current_url, "❌ Not on Data Ingestion Settingsn page"
            logging.info("-------Successfully Navigated to Data Ingestion Settings page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0021"
        tp_description = f"Navigate to Data Ingestion Settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesReconciliationMachingRulesSettlementReconciliationByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/matching-rules/settlement-reconciliation")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")     

            assert "/matching-rules/settlement-reconciliation" in driver.current_url, "❌ Not on settlement reconciliation matching page"
            logging.info("-------Successfully Navigated to settlement reconciliation matching page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0022"
        tp_description = f"Navigate to settlement reconciliation matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesReconciliationMachingRulesBankReconciliationByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/matching-rules/bank-reconciliation")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/matching-rules/bank-reconciliation" in driver.current_url, "❌ Not on bank reconciliation matching page"
            logging.info("-------Successfully Navigated to bank reconciliation matching page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0023"
        tp_description = f"Navigate to bank reconciliation matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesReconciliationSettlementReconciliationSettingsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/settlement-reconciliation-settings")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")            

            assert "/settlement-reconciliation-settings" in driver.current_url, "❌ Not on settlement reconciliation settings page"
            logging.info("-------Successfully Navigated to settlement reconciliation settingsg page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0024"
        tp_description = f"Navigate to settlement reconciliation settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesReconciliationBankReconciliationSettingsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/bank-reconciliation-settings")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/bank-reconciliation-settings" in driver.current_url, "❌ Not on bank reconciliation settings page"
            logging.info("-------Successfully Navigated to bank reconciliation settingsg page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0025"
        tp_description = f"Navigate to bank reconciliation settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesAccountingAccountingRulesByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/accounting-rules")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")          

            assert "/accounting-rules" in driver.current_url, "❌ Not on bank reconciliation settings page"
            logging.info("-------Successfully Navigated to accounting rules page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0026"
        tp_description = f"Navigate to accounting rules page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesAccountingAccountingPeriodsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/accounting-periods")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")            

            assert "/accounting-periods" in driver.current_url, "❌ Not on accounting periods page"
            logging.info("-------Successfully Navigated to accounting periods page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0027"
        tp_description = f"Navigate to accounting periods page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesAccountingChartsOfAccountsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/chart-accounts")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/chart-accounts" in driver.current_url, "❌ Not on charts of accounts page"
            logging.info("-------Successfully Navigated to charts of accounts page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0028"
        tp_description = f"Navigate to charts of accounts page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesAccountingSettingsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/accounting-settings")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/accounting-settings" in driver.current_url, "❌ Not on accounting settings page"
            logging.info("-------Successfully Navigated to accounting settings page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0029"
        tp_description = f"Navigate to accounting settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesGeneralSettingsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/general-settingst")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/general-settings" in driver.current_url, "❌ Not on accounting settings page"
            logging.info("-------Successfully Navigated to general settings page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0030"
        tp_description = f"Navigate to general settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesMerchantFeeRulesByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/fee-rules")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/fee-rules" in driver.current_url, "❌ Not on merchant fee rules page"
            logging.info("-------Successfully Navigated to merchant fee rules page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0031"
        tp_description = f"Navigate to merchant fee rules page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToCashForecastByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/dashboard/cash-forecastt")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/cash-forecast" in driver.current_url, "❌ Not on cash forecast page"
            logging.info("-------Successfully Navigated to cash forecast page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP001"
        tp_description = f"Navigate to cash forecast page"
        tkt_id= f"ADAD-0001"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateDashboardByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/dashboard")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")
            

            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP000"
        tp_description = f"Navigate to Dashboard page"
        tkt_id= f"ADAD-0000"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToFileDashboardByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/etl-files")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/etl-files" in driver.current_url, "❌ Not on File Dashboard page"
            logging.info("-------Successfully Navigated to File Dashboard page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0004"
        tp_description = f"Navigate to File Dashboard page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution="failed")  

class TestPointNavigateToFailedTransactionsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/failed-transactions")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/failed-transactions" in driver.current_url, "❌ Not on Failed Transactions page"            
            logging.info("-------Successfully Navigated to Failed Transactions page------")

            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0005"
        tp_description = f"Navigate to Failed Transactions page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataRateOfExchangeByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/roe")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/roe" in driver.current_url, "❌ Not on rate of exchange page"
            logging.info("-------Successfully Navigated to rate of exchange page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0032"
        tp_description = f"Navigate to rate of exchange page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataFxRateSourcesByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/fx-rate-sources")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")

            assert "/fx-rate-sources" in driver.current_url, "❌ Not on fx rate source page"
            logging.info("-------Successfully Navigated to fx rate source page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0033"
        tp_description = f"Navigate to fx rate source page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataFormOfPaymentsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/form-of-payments")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}")            

            assert "/form-of-payments" in driver.current_url, "❌ Not on form of payments page"
            logging.info("-------Successfully Navigated to form of payments page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0034"
        tp_description = f"Navigate to form of payments page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataPointOfSalesByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/point-of-sales")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "/point-of-sales" in driver.current_url, "❌ Not on point of sales page"
            logging.info("-------Successfully Navigated to point of sales page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0035"
        tp_description = f"Navigate to point of sales page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataPointOfSalesMerchantMappingByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/point-of-sales-merchant-mapping")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "/point-of-sales-merchant-mapping" in driver.current_url, "❌ Not on point of sales merchant mapping page"
            logging.info("-------Successfully Navigated to point of sales merchant mapping page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0036"
        tp_description = f"Navigate to point of sales merchant mapping page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataAcquirersByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/acquirers")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "/acquirers" in driver.current_url, "❌ Not on acquirers page"
            logging.info("-------Successfully Navigated to acquirers page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0037"
        tp_description = f"Navigate to acquirers page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataAcquirersMerchantsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/acquirer-merchants")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "/acquirer-merchants" in driver.current_url, "❌ Not on acquirers merchants page"
            logging.info("-------Successfully Navigated to acquirers merchants page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0038"
        tp_description = f"Navigate to acquirers merchants page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMasterDataSaleSourcesByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/sale-sources")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 
            
            assert "/sale-sources" in driver.current_url, "❌ Not on sale sources page"
            logging.info("-------Successfully Navigated to sale sources page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0039"
        tp_description = f"Navigate to sale sources page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToPendingItemsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/pending-items")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "/pending-items" in driver.current_url, "❌ Not on pending items page"
            logging.info("-------Successfully Navigated to pending items page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0008"
        tp_description = f"Navigate to pending items page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToProvisionalMismatchedItemsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/provisional-mismatched-items")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "/pending-items" in driver.current_url, "❌ Not on pending items page"
            logging.info("-------Successfully Navigated to Provisional Mismatched Items page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0009"
        tp_description = f"Navigate to Provisional Mismatched Itemspage"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToInstallmentsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/installments")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "/installments" in driver.current_url, "❌ Not on installments page"
            logging.info("-------Successfully Navigated to installments page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0010"
        tp_description = f"Navigate to installments page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToMatchedItemsMatchedByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/matched-items")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 
            

            assert "/matched-items" in driver.current_url, "❌ Not on Matched page"
            logging.info("-------Successfully Navigated to Matched page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0011"
        tp_description = f"Navigate to Matched page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToExceptionsByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/matched-items/exceptions")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "matched-items/exceptions" in driver.current_url, "❌ Not on Exceptions page"
            logging.info("-------Successfully Navigated to Exceptions page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0012"
        tp_description = f"Navigate to Exceptions page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToManualMatchingByLink(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/manual-matching")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            assert "manual-matching" in driver.current_url, "❌ Not on Manual Maching page"
            logging.info("-------Successfully Navigated to Manual Maching page------")
            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP0013"
        tp_description = f"Navigate to Manual Maching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateSetllmentsDisputesByLink(TestPoint):
    def __init__(self):
        def func(driver = webdriver):
            
            try:
                # Try navigating to a page
                driver.get("https://8x.staging.adad.io/settlement-disputes")
                logging.info("✅ Successfully navigated to the page.")

            except TimeoutException:
                logging.info("⏰ The page took too long to load!")

            except WebDriverException as e:
                logging.info(f"❌ Failed to open the link. Error: {e}") 

            # Assertion: check text or visibility  
            assert "/settlement-disputes" in driver.current_url, "❌ Not on settlement disputes page"                     
            logging.info("-------Successfully Navigated to settlement disputes page------")
            

            time.sleep(2)
        # Assign metadata separately
        tp_id = "TP000"
        tp_description = f"Navigate to settlement disputes page"
        tkt_id= f"ADAD-0014"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

