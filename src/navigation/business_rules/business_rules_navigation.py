from src.testpoint.testpoint_main import TestPoint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestPointNavigateToBusinesssRulesAlertTypeAffiliation(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")

            time.sleep(2)

            try :
                mached_items = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in mached_items.get_attribute("class"):
                logging.info("Successfully clicked the Alerts icon - ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR, "span.ng-tns-c35-136")
                click_icon.click()
                logging.info("Successfully clicked the Alerts icon --")

            time.sleep(3)

            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/ul/li/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Alert Type Afiliation item!")
            time.sleep(2)

            assert "/alert-type-affiliation" in driver.current_url, "❌ Not on Alert Type Afiliation page"
            logging.info("-------Successfully Navigated to Alert Type Afiliation page------")
        # Assign metadata separately
        tp_id = "TP0020"
        tp_description = f"Navigate to Alert Type Afiliation page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesDataIngestionSettings(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                data_ingestion = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in data_ingestion.get_attribute("class"):
                logging.info("Successfully clicked the Data ingestion icon - ")
            else:
                click_icon = driver.find_element(By.CSS_SELECTOR, "span.ng-tns-c35-137")
                click_icon.click()
                logging.info("Successfully clicked the Data ingestion icon --")

            time.sleep(3)

            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/ul/li/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the Data Ingestion Settings item!")
            time.sleep(2)

            assert "/settings" in driver.current_url, "❌ Not on Data Ingestion Settingsn page"
            logging.info("-------Successfully Navigated to Data Ingestion Settings page------")
        # Assign metadata separately
        tp_id = "TP0021"
        tp_description = f"Navigate to Data Ingestion Settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesReconciliationMachingRulesSettlementReconciliation(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                reconciliation = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a/span")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in reconciliation.get_attribute("class"):
                logging.info("Successfully clicked the reconciliation icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the reconciliation icon --")

            time.sleep(3)

            try :
                matching_rules = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in matching_rules.get_attribute("class"):
                logging.info("Successfully clicked the matching rules icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the matching rules icon --")

            time.sleep(3)




            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the settlement reconciliation item!")
            time.sleep(2)

            assert "/matching-rules/settlement-reconciliation" in driver.current_url, "❌ Not on settlement reconciliation matching page"
            logging.info("-------Successfully Navigated to settlement reconciliation matching page------")
        # Assign metadata separately
        tp_id = "TP0022"
        tp_description = f"Navigate to settlement reconciliation matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesReconciliationMachingRulesBankReconciliation(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                reconciliation = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in reconciliation.get_attribute("class"):
                logging.info("Successfully clicked the reconciliation icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a")
                click_icon.click()
                logging.info("Successfully clicked the reconciliation icon --")

            time.sleep(3)

            try :
                matching_rules = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in matching_rules.get_attribute("class"):
                logging.info("Successfully clicked the matching rules icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a")
                click_icon.click()
                logging.info("Successfully clicked the matching rules icon --")

            time.sleep(3)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a")
            sidebar_item.click()
            logging.info("Successfully clicked the bank reconciliation item!")
            time.sleep(2)

            assert "/matching-rules/bank-reconciliation" in driver.current_url, "❌ Not on bank reconciliation matching page"
            logging.info("-------Successfully Navigated to bank reconciliation matching page------")
        # Assign metadata separately
        tp_id = "TP0023"
        tp_description = f"Navigate to bank reconciliation matching page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesReconciliationSettlementReconciliationSettings(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                reconciliation = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in reconciliation.get_attribute("class"):
                logging.info("Successfully clicked the reconciliation icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a")
                click_icon.click()
                logging.info("Successfully clicked the reconciliation icon --")

            time.sleep(3)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a")
            sidebar_item.click()
            logging.info("Successfully clicked the settlement reconciliation settings item!")
            time.sleep(2)

            assert "/settlement-reconciliation-settings" in driver.current_url, "❌ Not on settlement reconciliation settings page"
            logging.info("-------Successfully Navigated to settlement reconciliation settingsg page------")
        # Assign metadata separately
        tp_id = "TP0024"
        tp_description = f"Navigate to settlement reconciliation settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesReconciliationBankReconciliationSettings(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                reconciliation = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in reconciliation.get_attribute("class"):
                logging.info("Successfully clicked the reconciliation icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a")
                click_icon.click()
                logging.info("Successfully clicked the reconciliation icon --")

            time.sleep(3)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a")
            sidebar_item.click()
            logging.info("Successfully clicked the bank reconciliation settings item!")
            time.sleep(2)

            assert "/bank-reconciliation-settings" in driver.current_url, "❌ Not on bank reconciliation settings page"
            logging.info("-------Successfully Navigated to bank reconciliation settingsg page------")
        # Assign metadata separately
        tp_id = "TP0025"
        tp_description = f"Navigate to bank reconciliation settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesAccountingAccountingRules(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                accounting = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon --")

            time.sleep(3)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/ul/li[1]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the accounting rules item!")
            time.sleep(2)

            assert "/accounting-rules" in driver.current_url, "❌ Not on bank reconciliation settings page"
            logging.info("-------Successfully Navigated to accounting rules page------")
        # Assign metadata separately
        tp_id = "TP0026"
        tp_description = f"Navigate to accounting rules page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesAccountingAccountingPeriods(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                accounting = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon --")

            time.sleep(3)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/ul/li[2]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the accounting periods item!")
            time.sleep(2)

            assert "/accounting-periods" in driver.current_url, "❌ Not on accounting periods page"
            logging.info("-------Successfully Navigated to accounting periods page------")
        # Assign metadata separately
        tp_id = "TP0027"
        tp_description = f"Navigate to accounting periods page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesAccountingChartsOfAccounts(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                accounting = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon --")

            time.sleep(3)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/ul/li[3]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the charts of accounts item!")
            time.sleep(2)

            assert "/chart-accounts" in driver.current_url, "❌ Not on charts of accounts page"
            logging.info("-------Successfully Navigated to charts of accounts page------")
        # Assign metadata separately
        tp_id = "TP0028"
        tp_description = f"Navigate to charts of accounts page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesAccountingSettings(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            try :
                accounting = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a")

            except Exception as e :
                logging.info(e)

            if "active-menuitem" in accounting.get_attribute("class"):
                logging.info("Successfully clicked the accounting icon - ")
            else:
                click_icon = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a")
                click_icon.click()
                logging.info("Successfully clicked the accounting icon --")

            time.sleep(3)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/ul/li[4]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the settings item!")
            time.sleep(2)

            assert "/accounting-settings" in driver.current_url, "❌ Not on accounting settings page"
            logging.info("-------Successfully Navigated to accounting settings page------")
        # Assign metadata separately
        tp_id = "TP0029"
        tp_description = f"Navigate to accounting settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesGeneralSettings(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[5]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the general settings item!")
            time.sleep(2)

            assert "/general-settings" in driver.current_url, "❌ Not on accounting settings page"
            logging.info("-------Successfully Navigated to general settings page------")
        # Assign metadata separately
        tp_id = "TP0030"
        tp_description = f"Navigate to general settings page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  

class TestPointNavigateToBusinesssRulesMerchantFeeRules(TestPoint):
    def __init__(self):
        
        def func(driver = webdriver):
            
            time.sleep(2)
            business_rules = driver.find_element(By.XPATH, "//span[text()='Business Rules']/parent::a")

            if "active-menuitem" in business_rules.get_attribute("class"):
                logging.info("Successfully clicked the Business Rules icon *")
            else:
                click_icon = driver.find_element(By.XPATH ,"/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/a/span")
                click_icon.click()
                logging.info("Successfully clicked the Business Rules icon **")
            time.sleep(2)


            sidebar_item = driver.find_element(By.XPATH, "/html/body/app-root/adad-frontend-layout/div/adad-frontend-sidebar/div/ul/li[9]/adad-frontend-sidebar-item/ul/li[6]/adad-frontend-sidebar-item/a/span")
            sidebar_item.click()
            logging.info("Successfully clicked the merchant fee rules item!")
            time.sleep(2)

            assert "/fee-rules" in driver.current_url, "❌ Not on merchant fee rules page"
            logging.info("-------Successfully Navigated to merchant fee rules page------")
        # Assign metadata separately
        tp_id = "TP0031"
        tp_description = f"Navigate to merchant fee rules page"
        tkt_id= f"*****"
        tp_status=f"ready"

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution= "failed")  