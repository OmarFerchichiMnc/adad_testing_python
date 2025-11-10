from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUIAddFilters, SaleUICheckIfSaleTableNotEmpty, SaleUIClickSearch, SaleUIFilterChannelType, SaleUIFilterCountry, SaleUIFilterFOPCode, SaleUIFilterFOPSubCode, SaleUIFilterFileID, SaleUIFilterPaymentDateRange, SaleUIFilterSaleID, SaleUIFilterSettledStatus


class AuditTrackSalesAdvancedFilters(TestCase):
    def __init__(self , payment_date_range = '', channel_type= '', country = '', file_id = '', fop_code = '',fop_sub_code = '', settled_status = '' ):
        super().__init__(id="Upload_sales_files", description="Upload sales files and check if the ingestion done correctly", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())
        # SaleUIFilterPaymentDateRange
        self.add_testpoint(SaleUIFilterPaymentDateRange(payment_date_range))
        # SaleUIFilterChannelType
        self.add_testpoint(SaleUIFilterChannelType(channel_type))
        self.add_testpoint(SaleUIFilterCountry(country))
        self.add_testpoint(SaleUIFilterFileID(file_id))
        self.add_testpoint(SaleUIAddFilters())
        self.add_testpoint(SaleUIFilterFOPCode(fop_code))
        self.add_testpoint(SaleUIFilterFOPSubCode(fop_sub_code))
        self.add_testpoint(SaleUIFilterSettledStatus(settled_status))
        
        self.add_testpoint(SaleUIClickSearch())
        self.add_testpoint(SaleUICheckIfSaleTableNotEmpty())
        