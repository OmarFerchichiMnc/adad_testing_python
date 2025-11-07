from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUICheckIfSaleTableNotEmpty, SaleUIClickSearch, SaleUIFilterPNROrderReference, SaleUIFilterSaleID


class AuditTrackSalesPNROrderReferenceFilters(TestCase):
    def __init__(self , pnr_order_reference):
        super().__init__(id="Testcase_Audit_Track_Pnr_Order_Reference_Filter", description="Extract pnr order reference from database and filter it and check if exists", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())

        self.add_testpoint(SaleUIFilterPNROrderReference(pnr_order_reference))
        self.add_testpoint(SaleUIClickSearch())
        self.add_testpoint(SaleUICheckIfSaleTableNotEmpty())