from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUIClickSearch, SaleUIFilterSaleID


class AuditTrackSalesSaleIDFilters(TestCase):
    def __init__(self , sale_id):
        super().__init__(id="Upload_sales_files", description="Upload sales files and check if the ingestion done correctly", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())

        self.add_testpoint(SaleUIFilterSaleID(sale_id))
        self.add_testpoint(SaleUIClickSearch())