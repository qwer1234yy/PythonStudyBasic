import unittest
from selenium import webdriver
from SMART import Smart_commons as Smart_commons
import SMART.Smart_pages.Smart_reports as Smart_reports
import SMART.Smart_tools.report_tools as report_tools


class Test_legacy_report(unittest.TestCase):
    driver = ''
    report_name = ''

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        if self.fail:
            report_tools.take_screenshot(self.driver, self.report_name + '-Failed-')
        else:
            report_tools.take_screenshot(self.driver, self.report_name)
        # self.driver.close()

    def test_ip_reports_standard(self):
        print('test_ip_reports_standard')
        Smart_commons.login_(self.driver)
        standard_or_enterprise = 'enterprise'
        if 'standard' in standard_or_enterprise:
            Smart_reports.reports.go_to_report_ip_Standard(self.driver)
        else:
            Smart_reports.reports.go_to_report_ip_Enterstand(self.driver)


        #standard_or_enterprise
        names = report_tools.read_report_names(standard_or_enterprise)
        fail = False
        for name in names:
            # name = 'Inpatient Flag Information'
            report_name = name
            Smart_reports.reports.find_report(self.driver, report_name=report_name)
            Smart_reports.reports.go_to_report_CS(self.driver, report_name=report_name)
            Smart_reports.reports.view_report(self.driver, report_name)
            Smart_reports.reports.switch_to_report_view_page(self.driver, report_name)

            # out of memory
            report_tools.out_of_memory_handle(self.driver, report_name)


            report_tools.take_screenshot(self.driver, report_name)
            Smart_reports.reports.close_report_view_window(self.driver)
            Smart_reports.reports.close_report_cs_page(self.driver)


if __name__ == '__main__':
    unittest.main()
