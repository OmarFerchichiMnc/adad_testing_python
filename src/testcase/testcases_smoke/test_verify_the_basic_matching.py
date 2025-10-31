from src.configuration.file_injection.file_injection import InjectFile
from src.configuration.utils.utils import adad_paths, sale_and_settlement_molecule_correct_files
from src.navigation.business_rules.business_rules_navigation import TestPointNavigateToBusinesssRulesReconciliationSettlementReconciliationSettings
from src.navigation.data_ingestion.data_ingestion_navigation import TestPointNavigateToFileDashboard
from src.navigation.navigation_by_link import TestPointNavigateToFileDashboardByLink, TestPointNavigateToManualMatchingByLink
from src.navigation.reconciliation.reconciliation_navigation import TestPointNavigateToManualMatching
from src.testcase.testcase_main import TestCase
from src.ui.business_rules.reconciliation.settlement_reconciliation_settings_ui import TriggerNow
from src.ui.data_ingestion.file_dashboard_ui import CheckIfFileIngested, FileDashboardUIFilterClickSearch, FileDashboardUIFilterFileID

class VerifyTheBasicMatching(TestCase):
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

        # Trigger basic matching
        self.add_testpoint(TestPointNavigateToManualMatchingByLink())
        self.add_testpoint(TriggerNow())