from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUICheckIfSaleTableNotEmpty, SaleUIClickSearch, SaleUIFilterPaymentID, SaleUIFilterSaleID


class AuditTrackSaleUIFilterPaymentID(TestCase):
    def __init__(self , sale_id):
        super().__init__(id="Testcase_Audit_Track_Sale_Payment_ID_Filter", description="Extract Payment ID from database and filter it and check if exists", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())

        self.add_testpoint(SaleUIFilterPaymentID(sale_id))
        self.add_testpoint(SaleUIClickSearch())
        self.add_testpoint(SaleUICheckIfSaleTableNotEmpty())