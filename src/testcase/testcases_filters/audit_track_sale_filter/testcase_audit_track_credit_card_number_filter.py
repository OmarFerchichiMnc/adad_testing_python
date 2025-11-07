from src.navigation.navigation_by_link import TestPointNavigateToAuditTrackSaleByLink
from src.testcase.testcase_main import TestCase
from src.ui.audit_track.sale_ui import SaleUICheckIfSaleTableNotEmpty, SaleUIClickSearch, SaleUIFilterCreditCard4LastDegits, SaleUIFilterCreditCardBIN, SaleUIFilterSelectCreditCardNumberToFilter


class AuditTrackSalesCreditCardNumberFilters(TestCase):
    def __init__(self , card_bin ,card_4_last_degits):
        super().__init__(id="Testcase_Audit_Track_Credit_Card_Number_Filter", description="Extract Credit Card bin and Credit Card 4 last degits from database and filter it and check if exists", ticket_id="TKT001")

        #navigate to audit track sale
        self.add_testpoint(TestPointNavigateToAuditTrackSaleByLink())

        self.add_testpoint(SaleUIFilterSelectCreditCardNumberToFilter())
        self.add_testpoint(SaleUIFilterCreditCardBIN(card_bin))
        self.add_testpoint(SaleUIFilterCreditCard4LastDegits(card_4_last_degits))

        self.add_testpoint(SaleUIClickSearch())
        self.add_testpoint(SaleUICheckIfSaleTableNotEmpty())