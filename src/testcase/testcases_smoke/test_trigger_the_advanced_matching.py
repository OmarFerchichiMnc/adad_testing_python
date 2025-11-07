from src.configuration.file_injection.file_injection import InjectFile, WaitForFileInjection
from src.navigation.business_rules.business_rules_navigation import TestPointNavigateToBusinesssRulesReconciliationSettlementReconciliationSettings
from src.navigation.data_ingestion.data_ingestion_navigation import TestPointNavigateToFileDashboard
from src.navigation.navigation_by_link import TestPointNavigateToBusinesssRulesReconciliationSettlementReconciliationSettingsByLink, TestPointNavigateToFileDashboardByLink, TestPointNavigateToMatchedItemsMatchedByLink
from src.navigation.reconciliation.reconciliation_navigation import TestPointNavigateToMatchedItemsMatched
from src.testcase.testcase_main import TestCase
from src.ui.business_rules.reconciliation.settlement_reconciliation_settings_ui import TriggerNow
from src.ui.data_ingestion.file_dashboard_ui import CheckIfFileIngested, FileDashboardUIFilterClickSearch, FileDashboardUIFilterFileID
from src .configuration.utils.utils import sale_and_settlement_molecule_correct_files, adad_paths
from src.ui.reconciliation.matched_items.matched_ui import SaleUICheckIfMatchingDoneCorrectly

class TriggerTheAdvancedMatching(TestCase):
    def __init__(self):
        super().__init__(id="trigger_the_advanced_matching", description="Upload sales and settlements files and check if the advanced matching done correctly", ticket_id="TKT001")

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


        # Trigger basic matching
        self.add_testpoint(TestPointNavigateToBusinesssRulesReconciliationSettlementReconciliationSettingsByLink())
        self.add_testpoint(TriggerNow())
        self.add_testpoint(TestPointNavigateToMatchedItemsMatchedByLink())
        self.add_testpoint(SaleUICheckIfMatchingDoneCorrectly('1'))