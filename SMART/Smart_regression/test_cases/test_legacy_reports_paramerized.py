import unittest
from parameterized import parameterized, param
from selenium import webdriver
from SMART import Smart_commons as Smart_commons
import SMART.Smart_pages.Smart_reports as Smart_reports
import SMART.Smart_tools.report_tools as report_tools
import SMART.Smart_common.Smart_actions as Smart_actions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def get_report_names():
    names = report_tools.read_report_names('standard')
    return names


class Test_legacy_report(unittest.TestCase):
    driver = ''
    report_name = ''
    fail = False

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        if self.fail:
            report_tools.take_screenshot(self.driver, self.report_name + '-Failed-')
        self.driver.close()

    @parameterized.expand(get_report_names)
    def test_ip_reports_standard(self, name):

        self.report_name = name
        report_name = name

        try:
            Smart_commons.login_(self.driver)
            Smart_reports.reports.go_to_report_ip_Standard(self.driver)
            Smart_reports.reports.find_report(self.driver, report_name=report_name)
            Smart_reports.reports.go_to_report_CS(self.driver, report_name=report_name)
            Smart_reports.reports.view_report(self.driver)
            Smart_reports.reports.switch_to_report_view_page(self.driver)
            report_tools.take_screenshot(self.driver, self.report_name)
            # out of memory
            report_tools.out_of_memory_handle(self.driver)
            # pass
        except Exception as e:
            print(e)
            fail = True
            pass




if __name__ == '__main__':
    unittest.main()
