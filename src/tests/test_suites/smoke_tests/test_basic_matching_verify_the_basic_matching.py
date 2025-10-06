import time
from src.testcase.testcases_smoke.test_verify_the_basic_matching import VerifyTheBasicMatching


def test_2(driver):
    tc = VerifyTheBasicMatching()
    tc.run(driver)
    tc.export_to_json()