
import time
import requests
from src.api.api_testpoints import TestPointGetUsers
import logging
import os

from src.navigation.accounting.accounting_navigation import TestPointNavigateToAccountingJournal, TestPointNavigateToImbalancedJournalEntries, TestPointNavigateToPostToLedger, TestPointNavigateToTrialBalance, TestPointNavigateToUnaccountedEvents
from src.navigation.alerts.alerts_navigation import TestPointNavigateToAlertManagement, TestPointNavigateToReconciliationAlerts
from src.navigation.audit_track.audit_track_navigation import TestPointNavigateToAuditTrackSale, TestPointNavigateToAuditTrackSettlement
from src.navigation.business_rules.business_rules_navigation import TestPointNavigateToBusinesssRulesAccountingAccountingPeriods, TestPointNavigateToBusinesssRulesAccountingAccountingRules, TestPointNavigateToBusinesssRulesAccountingChartsOfAccounts, TestPointNavigateToBusinesssRulesAccountingSettings, TestPointNavigateToBusinesssRulesAlertTypeAffiliation, TestPointNavigateToBusinesssRulesDataIngestionSettings, TestPointNavigateToBusinesssRulesGeneralSettings, TestPointNavigateToBusinesssRulesMerchantFeeRules, TestPointNavigateToBusinesssRulesReconciliationBankReconciliationSettings, TestPointNavigateToBusinesssRulesReconciliationMachingRulesBankReconciliation, TestPointNavigateToBusinesssRulesReconciliationMachingRulesSettlementReconciliation, TestPointNavigateToBusinesssRulesReconciliationSettlementReconciliationSettings
from src.navigation.cash_forecast.cash_forecast_navigation import TestPointNavigateToCashForecast
from src.navigation.dashboard.dashboard_navigation import TestPointNavigateDashboard
from src.navigation.data_ingestion.data_ingestion_navigation import TestPointNavigateToFailedTransactions, TestPointNavigateToFileDashboard
from src.navigation.master_data.master_data_navigation import TestPointNavigateToMasterDataAcquirers, TestPointNavigateToMasterDataAcquirersMerchants, TestPointNavigateToMasterDataFormOfPayments, TestPointNavigateToMasterDataFxRateSources, TestPointNavigateToMasterDataPointOfSales, TestPointNavigateToMasterDataPointOfSalesMerchantMapping, TestPointNavigateToMasterDataRateOfExchange, TestPointNavigateToMasterDataSaleSources
from src.navigation.reconciliation.reconciliation_navigation import TestPointNavigateToExceptions, TestPointNavigateToInstallments, TestPointNavigateToMatchedItemsMatched, TestPointNavigateToManualMatching, TestPointNavigateToPendingItems, TestPointNavigateToProvisionalMismatchedItems
from src.navigation.settlements_disputes.settlements_disputes_navigation import TestPointNavigateSetllmentsDisputes
from src.testpoint.testpoint_main import TestPoint
from src.ui.audit_track.sale_ui import SaleUIAddFilters, SaleUICheckIfFileFound, SaleUIClickSearch, SaleUIFilterChannelType, SaleUIFilterPaymentDateRange, SaleUIFilterSaleID
from src.ui.audit_track.settlement_ui import SettlementUIAddFilters, SettlementUICheckIfFileFound, SettlementUIClickSearch, SettlementUIFilterCustomerAcquirer, SettlementUIFilterPNROrderReference, SettlementUIFilterPaymentDateRange, SettlementUIFilterSettlementID, SettlementUIPaymentOrderCheckIfFileFound, SettlementUIPaymentOrderClickSearch, SettlementUIPaymentOrderFilterCustomerAcquirer, SettlementUIPaymentOrderFilterPaymentDateRange, SettlementUISelectSettlementOrPaymentOrder
from src.ui.business_rules.reconciliation.manual_matching_ui import ManualMatchingUISaleFilterChannelType, ManualMatchingUISaleFilterDocumentNumber, ManualMatchingUISaleFilterPNR, ManualMatchingUISaleFilterPaymentDateRange, ManualMatchingUISettlementFilterCustomerAcquirer, ManualMatchingUISettlementFilterDocumentNumber, ManualMatchingUISettlementFilterPNR, ManualMatchingUISettlementFilterPaymentDateRange
from src.ui.dashboard_ui import DashboardUISaleFilterDateRange
from src.ui.data_ingestion.file_dashboard_ui import  CheckIfFileIngested, FileDashboardUIFilterClickSearch, FileDashboardUIFilterFileID

 
def test_navigate_to_dashboard(driver):
    TestPointNavigateDashboard().func(driver)
    
def test_navigate_to_cash_forecast(driver):
    TestPointNavigateToCashForecast().func(driver)

def test_navigate_to_alert_management(driver):
    TestPointNavigateToAlertManagement().func(driver)

def test_navigate_to_reconciliation_alerts(driver):
    TestPointNavigateToReconciliationAlerts().func(driver)

def test_navigate_to_file_dashboard(driver):
    TestPointNavigateToFileDashboard().func(driver)

def test_navigate_to_failed_transactions(driver):
    TestPointNavigateToFailedTransactions().func(driver)

def test_navigate_to_audit_track_sale(driver):
    TestPointNavigateToAuditTrackSale().func(driver)

def test_navigate_to_audit_track_settlement(driver):
    TestPointNavigateToAuditTrackSettlement().func(driver)

def test_navigate_to_pending_items(driver):
    TestPointNavigateToPendingItems().func(driver)

def test_navigate_to_provisional_mismatched_items(driver):
    TestPointNavigateToProvisionalMismatchedItems().func(driver)

def test_navigate_to_installments(driver):
    TestPointNavigateToInstallments().func(driver)

def test_navigate_to_matched_items_matched(driver):
    TestPointNavigateToMatchedItemsMatched().func(driver)

def test_navigate_to_exceptions(driver):
    TestPointNavigateToExceptions().func(driver)

def test_navigate_to_manual_matching(driver):
    TestPointNavigateToManualMatching().func(driver)

def test_navigate_to_settlement_disputes(driver):
    TestPointNavigateSetllmentsDisputes().func(driver)

def test_navigate_to_accounting_journal(driver):
    TestPointNavigateToAccountingJournal().func(driver)

def test_navigate_to_unaccounted_events(driver):
    TestPointNavigateToUnaccountedEvents().func(driver)

def test_navigate_to_imbalanced_journal_entries(driver):
    TestPointNavigateToImbalancedJournalEntries().func(driver)

def test_navigate_to_trial_balance(driver):
    TestPointNavigateToTrialBalance().func(driver)

def test_navigate_to_post_to_ledger(driver):
    TestPointNavigateToPostToLedger().func(driver)

def test_navigate_to_alert_type_affiliation(driver):
    TestPointNavigateToBusinesssRulesAlertTypeAffiliation().func(driver)

def test_navigate_to_data_ingestion_settings(driver):
    TestPointNavigateToBusinesssRulesDataIngestionSettings().func(driver)
  
def test_navigate_to_reconciliation_matching_rules_settlement_reconciliation(driver):
    TestPointNavigateToBusinesssRulesReconciliationMachingRulesSettlementReconciliation().func(driver)

def test_navigate_to_reconciliation_matching_rules_bank_reconciliation(driver):
    TestPointNavigateToBusinesssRulesReconciliationMachingRulesBankReconciliation().func(driver)
   

def test_navigate_to_reconciliation_settlement_reconciliation_settings(driver):
    TestPointNavigateToBusinesssRulesReconciliationSettlementReconciliationSettings().func(driver)

def test_navigate_to_reconciliation_bank_reconciliation_settings(driver):
    TestPointNavigateToBusinesssRulesReconciliationBankReconciliationSettings().func(driver)
   

def test_navigate_to_accounting_rules(driver):
    TestPointNavigateToBusinesssRulesAccountingAccountingRules().func(driver)

def test_navigate_to_accounting_periods(driver):
    TestPointNavigateToBusinesssRulesAccountingAccountingPeriods().func(driver)

def test_navigate_to_accounting_charts_of_accounts(driver):
    TestPointNavigateToBusinesssRulesAccountingChartsOfAccounts().func(driver)

def test_navigate_to_accounting_settings(driver):
    TestPointNavigateToBusinesssRulesAccountingSettings().func(driver)

def test_navigate_to_general_settings(driver):
    TestPointNavigateToBusinesssRulesGeneralSettings().func(driver)

def test_navigate_to_merchant_fee_rules(driver):
    TestPointNavigateToBusinesssRulesMerchantFeeRules().func(driver)

def test_navigate_to_roe(driver):
    TestPointNavigateToMasterDataRateOfExchange().func(driver)

def test_navigate_to_fx_rate_sources(driver):
    TestPointNavigateToMasterDataFxRateSources().func(driver)

def test_navigate_to_form_of_payments(driver):
    TestPointNavigateToMasterDataFormOfPayments().func(driver)

def test_navigate_to_point_of_sales(driver):
    TestPointNavigateToMasterDataPointOfSales().func(driver)

def test_navigate_to_point_of_sales_merchant_mapping(driver):
    TestPointNavigateToMasterDataPointOfSalesMerchantMapping().func(driver)

def test_navigate_to_acquirers(driver):
    TestPointNavigateToMasterDataAcquirers().func(driver)

def test_navigate_to_acquirers_merchants(driver):
    TestPointNavigateToMasterDataAcquirersMerchants().func(driver)

def test_navigate_to_sale_sources(driver):
    TestPointNavigateToMasterDataSaleSources().func(driver)

def test_navigate_to_dashboard_play(driver):
   
    TestPointNavigateToFileDashboard().run(driver)
    FileDashboardUIFilterFileID("01K422W3NT8ENSR2DFZETRYVJF").run(driver)
    FileDashboardUIFilterClickSearch().run(driver)
    CheckIfFileIngested().run(driver)

def test_manual_matching(driver):
    TestPointNavigateToManualMatching().run(driver)
    ManualMatchingUISaleFilterPaymentDateRange("01/08/2025 - 31/08/2025").run(driver)
    ManualMatchingUISaleFilterChannelType("INDIRECT - Sale").run(driver)
    ManualMatchingUISaleFilterPNR("2655665").run(driver)
    ManualMatchingUISaleFilterDocumentNumber("2655665").run(driver)

    ManualMatchingUISettlementFilterPaymentDateRange("01/08/2025 - 31/08/2025").run(driver)
    ManualMatchingUISettlementFilterCustomerAcquirer("adyen").run(driver)
    ManualMatchingUISettlementFilterPNR("2655665").run(driver)
    ManualMatchingUISettlementFilterDocumentNumber("2655665").run(driver)

def test_manual_matching_try_add_filter(driver):
    TestPointNavigateToAuditTrackSale().run(driver)
    SaleUIFilterPaymentDateRange("01/01/2025 - 30/01/2025").run(driver)
    SaleUIFilterChannelType("INDIRECT - Sale").run(driver)
   
    #SaleUIFilterSaleID("wherever").run(driver)
    SaleUIClickSearch().run(driver)
    SaleUICheckIfFileFound().run(driver)

def test_dashboard_filter_date(driver) :
    TestPointNavigateDashboard().func(driver)
    DashboardUISaleFilterDateRange("01/01/2025 - 30/01/2025").func(driver)

def test_settlement_filter_date(driver) :
    TestPointNavigateToAuditTrackSettlement().func(driver)
    SettlementUIFilterPaymentDateRange("01/01/2025 - 30/01/2025").func(driver)
    SettlementUIFilterCustomerAcquirer("adyen").func(driver)
    SettlementUIFilterPNROrderReference("hfgfjj").func(driver)
    
    SettlementUIFilterSettlementID("5155").func(driver)

def test_settlement_add_filter(driver) :
    TestPointNavigateToAuditTrackSettlement().func(driver)
    SettlementUIAddFilters().func(driver)
    SettlementUIAddFilters().func(driver)
    SettlementUIClickSearch().func(driver)
    SettlementUICheckIfFileFound().func(driver)
   
def test_select_settlemnt_or_payment_order(driver) :
    TestPointNavigateToAuditTrackSettlement().func(driver) 
    SettlementUISelectSettlementOrPaymentOrder("Payment Order").func(driver)
    SettlementUISelectSettlementOrPaymentOrder().func(driver)
    SettlementUISelectSettlementOrPaymentOrder("Payment Order").func(driver)
    SettlementUISelectSettlementOrPaymentOrder("Settlement").func(driver)

def test_payment_filters(driver) :
    TestPointNavigateToAuditTrackSettlement().func(driver)
    SettlementUIPaymentOrderFilterPaymentDateRange("01/01/2025 - 30/01/2025").func(driver)
    SettlementUIPaymentOrderFilterCustomerAcquirer("adyen").func(driver)
    SettlementUIPaymentOrderClickSearch().func(driver)
    SettlementUIPaymentOrderCheckIfFileFound().func(driver)
    