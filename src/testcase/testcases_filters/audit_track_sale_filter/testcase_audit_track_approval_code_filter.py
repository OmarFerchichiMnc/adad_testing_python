from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUICheckIfSaleTableNotEmpty, SaleUIClickSearch, SaleUIFilterApprovalCode, SaleUIFilterSaleID


class AuditTrackSaleApprovalCodeFilters(TestCase):
    def __init__(self , approval_code):
        super().__init__(id="Testcase_Audit_Track_Approval_Code_Filter", description="Extract Approval Code from database and filter it and check if exists", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())

        self.add_testpoint(SaleUIFilterApprovalCode(approval_code))
        self.add_testpoint(SaleUIClickSearch())
        self.add_testpoint(SaleUICheckIfSaleTableNotEmpty())