import time

import pytest
from src.testcase.testcases_filters.testcase_audit_track_sale import PendingSalesFilters
list_date = ["08/09/2025 - 09/09/2025","08/08/2025 - 09/08/2025","08/10/2025 - 09/10/2025"]
list_channel_type = ["INDIRECT - Sale","DIRECT - HOT_v22"]
list_sale_id = ["" , "01K6N8BTM9KKD0WX8M4FXWEKRT","01K6N8BTMB1MGV5KMD31XD33YB","01K6N8BTMCC3GB96Q0HQV8NXRZ",
                "01K6N8BTMMFN2XZHFRD4R2DM7S","01K6N8BTMSYD4V7DC03BRCBWYH","01K6N8BTMT29XTAKC6ET0KYYA7",
                "01K6N8BTPP0NEQCADTMCAQ7S34","01K6N8BTPY4GBD3SR9BT0CQ79J","01K6N8BTQ6PR8BKAVNF5E9KRPT",
                "01K6N8BTQETXB9H8JX2QTEZWJY","01K6WJTNJHAMD8VKCYESRK84QR"]

@pytest.mark.parametrize("date",list_date)
@pytest.mark.parametrize("channel_type",list_channel_type)
@pytest.mark.parametrize("sale_id",list_sale_id)
def test_2(driver, date , channel_type , sale_id):
    tc = PendingSalesFilters(date, channel_type, sale_id)
    tc.run(driver)
    tc.export_to_json()
