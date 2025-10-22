from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUIClickSearch, SaleUIFilterDocumentNumber, SaleUIFilterSaleID


class AuditTrackSalesDocumentNumberFilters(TestCase):
    def __init__(self , document_number):
        super().__init__(id="Upload_sales_files", description="Upload sales files and check if the ingestion done correctly", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())

        self.add_testpoint(SaleUIFilterDocumentNumber(document_number))
        self.add_testpoint(SaleUIClickSearch())