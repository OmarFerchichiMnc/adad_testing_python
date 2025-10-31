from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUICheckIfSaleTableNotEmpty, SaleUIClickSearch, SaleUIFilterSaleID


class AuditTrackSalesAdvancedFilters(TestCase):
    def __init__(self , payment_date_range = '', channel_type= '', country = '', file_id = '', fop_code = '',fop_sub_code = '', settled_status = '' ):
        super().__init__(id="Upload_sales_files", description="Upload sales files and check if the ingestion done correctly", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())
        # SaleUIFilterPaymentDateRange
        # SaleUIFilterChannelType
        
        self.add_testpoint(SaleUIClickSearch())
        self.add_testpoint(SaleUICheckIfSaleTableNotEmpty())
        