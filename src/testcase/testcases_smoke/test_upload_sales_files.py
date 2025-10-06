from src.configuration.file_injection.file_injection import InjectFile
from src.configuration.file_injection.inject_try import ExecuteUpload, PrepareUpload
from src.configuration.file_injection.inject_try import BastionSSMForward, KillBastionSSM
from src.configuration.utils.utils import adad_paths, sale_and_settlement_molecule_correct_files
from src.navigation.data_ingestion.data_ingestion_navigation import TestPointNavigateToFileDashboard
from src.testcase.testcase_main import TestCase
from src.ui.data_ingestion.file_dashboard_ui import CheckIfFileIngested, FileDashboardUIFilterClickSearch, FileDashboardUIFilterFileID


class UploadSalesFiles(TestCase):
    def __init__(self):
        super().__init__(id="Upload_sales_files", description="Upload sales files and check if the ingestion done correctly", ticket_id="TKT001")

        # Define all test points inside this test case
        # Ingestion of sale file
        self.add_testpoint(InjectFile(sale_and_settlement_molecule_correct_files.sale_path_for_molecule,adad_paths.sales,sale_and_settlement_molecule_correct_files.sale_file_name))      
        self.add_testpoint(TestPointNavigateToFileDashboard())
        self.add_testpoint(FileDashboardUIFilterClickSearch())
        self.add_testpoint(CheckIfFileIngested(sale_and_settlement_molecule_correct_files.sale_file_name))
