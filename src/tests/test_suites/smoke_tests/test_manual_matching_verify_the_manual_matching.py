from src.testcase.testcases_smoke.test_upload_settlements_files import UploadSattlementsFiles
from src.testcase.testcases_smoke.test_verify_the_manual_matching import VerifyTheManualMatching


def test_1(driver):
    tc = VerifyTheManualMatching()
    tc.run(driver)
    tc.export_to_json()