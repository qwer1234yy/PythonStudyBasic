import unittest
from selenium import webdriver
from SMART import Smart_commons as Smart_commons
import SMART.Smart_pages.Smart_reports as Smart_reports
import SMART.Smart_tools.report_tools as report_tools
import SMART.Smart_common.Smart_actions as Smart_actions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Test_legacy_report(unittest.TestCase):

    driver = ''
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_ip_reports_standard(self):
        print('test_ip_reports_standard')
        Smart_commons.login_(self.driver)
        Smart_reports.reports.go_to_report_ip_Standard(self.driver)

        names = report_tools.read_report_names('standard')

        for name in names:
            report_name = name
            Smart_reports.reports.find_report(self.driver, report_name=report_name)
            Smart_reports.reports.go_to_report_CS(self.driver, report_name= report_name)
            Smart_reports.reports.view_report(self.driver)
            Smart_reports.reports.switch_to_report_view_page(self.driver)

            # out of memory
            Smart_reports.reports.out_of_memory_handle(self.driver)

            report_tools.take_screenshot(self.driver, report_name)
            Smart_reports.reports.close_report_view_window(self.driver)
            Smart_reports.reports.close_report_cs_page(self.driver)


    # def test_ip_reports_enterprise(self):
    #     print('test_ip_reports_enterprise')
    #     # SC.login_(self.driver)
    #
    # def test_op_reports_standard(self):
    #     print('test_op_reports_standard')
    #     # SC.login_(self.driver)
    #
    # def test_op_reports_enterprise(self):
    #     print('test_op_reports_enterprise')
    #     # SC.login_(self.driver)


if __name__ == '__main__':

    unittest.main()

