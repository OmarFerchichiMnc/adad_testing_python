from src.configuration.file_injection.file_injection import InjectFile
from src.configuration.utils.utils import adad_paths, sale_and_settlement_molecule_correct_files
from src.navigation.audit_track.audit_track_navigation import TestPointNavigateToAuditTrackSale
from src.navigation.data_ingestion.data_ingestion_navigation import TestPointNavigateToFileDashboard
from src.navigation.navigation_by_link import TestPointNavigateToFileDashboardByLink, TestPointNavigateToManualMatchingByLink, TestPointNavigateToMatchedItemsMatchedByLink
from src.navigation.reconciliation.reconciliation_navigation import TestPointNavigateToManualMatching, TestPointNavigateToMatchedItemsMatched
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUIAddFilters, SaleUIFilterChannelType, SaleUIFilterPaymentDateRange, SaleUIFilterSaleID
from src.ui.business_rules.reconciliation.manual_matching_ui import ManualMatchingUIConfirmMatching, ManualMatchingUIMatchSaleAndSettlement, ManualMatchingUIMatchSaleAndSettlementClickYes, ManualMatchingUISaleClickCheckBox, ManualMatchingUISaleClickSearch, ManualMatchingUISaleFilterChannelType, ManualMatchingUISaleFilterDocumentNumber, ManualMatchingUISaleFilterPNR, ManualMatchingUISaleFilterPaymentDateRange, ManualMatchingUISettlementClickCheckBox, ManualMatchingUISettlementClickSearch, ManualMatchingUISettlementFilterCustomerAcquirer, ManualMatchingUISettlementFilterDocumentNumber, ManualMatchingUISettlementFilterPNR, ManualMatchingUISettlementFilterPaymentDateRange
from src.ui.business_rules.reconciliation.settlement_reconciliation_settings_ui import TriggerNow
from src.ui.data_ingestion.file_dashboard_ui import CheckIfFileIngested, FileDashboardUIFilterClickSearch
from src.ui.reconciliation.matched_items.matched_ui import SaleUICheckIfMatchingDoneCorrectly


class VerifyTheManualMatching(TestCase):
    def __init__(self):
        super().__init__(id="verify_the_basic_matching", description="Upload sales and settlements files and check if the basic matching done correctly", ticket_id="TKT001")

         # Ingestion of sale file
        self.add_testpoint(InjectFile(sale_and_settlement_molecule_correct_files.sale_path_for_molecule,adad_paths.sales,sale_and_settlement_molecule_correct_files.sale_file_name))      
        self.add_testpoint(TestPointNavigateToFileDashboardByLink())
        self.add_testpoint(FileDashboardUIFilterClickSearch())
        self.add_testpoint(CheckIfFileIngested(sale_and_settlement_molecule_correct_files.sale_file_name))

        # Ingestion of settlement file
        self.add_testpoint(InjectFile(sale_and_settlement_molecule_correct_files.settlement_path_for_molecule,adad_paths.setllement,sale_and_settlement_molecule_correct_files.settlement_file_name))      
        self.add_testpoint(TestPointNavigateToFileDashboardByLink())
        self.add_testpoint(FileDashboardUIFilterClickSearch())
        self.add_testpoint(CheckIfFileIngested(sale_and_settlement_molecule_correct_files.settlement_file_name))


        #Manual matching
        self.add_testpoint(TestPointNavigateToManualMatchingByLink())

        # Search of sale file
        self.add_testpoint(ManualMatchingUISaleFilterPaymentDateRange(sale_and_settlement_molecule_correct_files.payment_date_range))
        self.add_testpoint(ManualMatchingUISaleFilterChannelType("INDIRECT - Sale"))
        self.add_testpoint(ManualMatchingUISaleFilterPNR("QNR1Y1"))
        self.add_testpoint(ManualMatchingUISaleClickSearch())
        self.add_testpoint(ManualMatchingUISaleClickCheckBox())
        
       
        # Search of settlement file
        self.add_testpoint(ManualMatchingUISettlementFilterPaymentDateRange(sale_and_settlement_molecule_correct_files.settlement_date_range))
        self.add_testpoint(ManualMatchingUISettlementFilterCustomerAcquirer("Settlement"))
        self.add_testpoint(ManualMatchingUISettlementFilterPNR("QNR1Y1"))
        self.add_testpoint(ManualMatchingUISettlementClickSearch())
        self.add_testpoint(ManualMatchingUISettlementClickCheckBox())


        self.add_testpoint(ManualMatchingUIConfirmMatching())
        self.add_testpoint(ManualMatchingUIMatchSaleAndSettlement())
        self.add_testpoint(ManualMatchingUIMatchSaleAndSettlementClickYes())
        
        self.add_testpoint(TestPointNavigateToMatchedItemsMatchedByLink())
        self.add_testpoint(SaleUICheckIfMatchingDoneCorrectly('1'))
