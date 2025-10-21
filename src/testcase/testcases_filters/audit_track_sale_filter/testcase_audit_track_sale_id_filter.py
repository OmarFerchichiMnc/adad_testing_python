from src.configuration.file_injection.file_injection import InjectFile
from src.configuration.file_injection.inject_try import ExecuteUpload, PrepareUpload
from src.configuration.file_injection.inject_try import BastionSSMForward, KillBastionSSM
from src.configuration.utils.utils import adad_paths, sale_and_settlement_molecule_correct_files
from src.navigation.audit_track.audit_track_navigation import TestPointNavigateToAuditTrackSale
from src.navigation.data_ingestion.data_ingestion_navigation import TestPointNavigateToFileDashboard
from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUIAddFilters, SaleUIClickSearch, SaleUIFilterChannelType, SaleUIFilterPaymentDateRange, SaleUIFilterSaleID
from src.ui.data_ingestion.file_dashboard_ui import CheckIfFileIngested, FileDashboardUIFilterClickSearch, FileDashboardUIFilterFileID




class AuditTrackSalesSaleIDFilters(TestCase):
    def __init__(self , sale_id):
        super().__init__(id="Upload_sales_files", description="Upload sales files and check if the ingestion done correctly", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())

        self.add_testpoint(SaleUIFilterSaleID(sale_id))
        self.add_testpoint(SaleUIClickSearch())