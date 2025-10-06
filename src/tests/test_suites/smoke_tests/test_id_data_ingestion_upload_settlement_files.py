from src.testcase.testcases_smoke.test_upload_settlements_files import UploadSattlementsFiles


def test_1(driver):
    tc = UploadSattlementsFiles()
    tc.run(driver)
    tc.export_to_json()