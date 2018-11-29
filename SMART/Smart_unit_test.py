import unittest,time
import SMART.Smart_commons as SC
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_wait(self):
        driver = webdriver.Firefox()
        SC.login_(driver)

        # Click "inpatient"
        inpatient = driver.find_element_by_id('aModuleSIP101')
        time.sleep(10)
        inpatient.click()

        # Click "report"
        report = driver.find_element_by_id('aIPModuleWorkplans')
        report.click()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
