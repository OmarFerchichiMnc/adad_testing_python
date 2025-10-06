from src.testcase.testcases_smoke.test_upload_sales_files import UploadSalesFiles


def test_1(driver):
    tc = UploadSalesFiles()
    tc.run(driver)
    tc.export_to_json()