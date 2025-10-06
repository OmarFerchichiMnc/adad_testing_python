import time
from src.testcase.testcases_smoke.test_trigger_the_advanced_matching import TriggerTheAdvancedMatching

def test_2(driver):
    tc = TriggerTheAdvancedMatching()
    tc.run(driver)
    tc.export_to_json()










