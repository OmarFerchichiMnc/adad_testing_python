import time
from src.testcase.testcases_filters.testcase_audit_track_sale import PendingSalesFilters
list_date = ["08/09/2025 - 09/09/2025","08/08/2025 - 09/08/2025","08/10/2025 - 09/10/2025"]

def test_2(driver):
    tc = PendingSalesFilters(list_date)
    tc.run(driver)
    tc.export_to_json()
