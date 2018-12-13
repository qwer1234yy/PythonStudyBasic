import unittest,time
from selenium import webdriver
import SMART.Smart_commons as SC
import SMART.Smart_com_acts as ACT
from selenium.webdriver.common.by import By
import SMART.Smart_reports as reports
import SMART.Smart_base_driver as drivers


class MyTestCase(unittest.TestCase):

    driver = drivers.driver_firefox()
    def setUp(self):

        print('setup')
    def test_enterprise_reports(self):

        reports_name_cases = SC.read_file_report_names_as_list('enterprise')
        report_names = []
        report_case_num = []
        for i in reports_name_cases:
            report_names.append(reports_name_cases[i])
            report_case_num.append(i)
        driver = self.driver
        SC.login_(driver)
        reports.reports.go_to_op_enterprise(driver)
        for i in range(0, report_names.__len__()-1):
            report_name = report_names[i]
            self.driver.save_screenshot('../pictures/' + report_name + '.png')
            reports.reports.find_report(driver, report_name)
            reports.reports.go_to_report_CS(driver, report_name)
            reports.reports.add_filters_besides_default_ones(driver)
            reports.reports.view_report(driver)
            reports.reports.switch_to_report_view_page(driver, report_name, report_case_num[i])
            reports.reports.close_report_view_window(driver)
            reports.reports.close_report_cs_page(driver)

    def test_standard_reports(self):
        reports_name_cases = SC.read_file_report_names_as_list('standard')

        report_names = []
        report_case_num = []

        for i in reports_name_cases:
            report_names.append(reports_name_cases[i])
            report_case_num.append(i)

        driver = self.driver
        SC.login_(driver)
        reports.reports.go_to_op_enterprise(driver)
        reports.reports.go_to_op_standard(driver)

        for i in range(0, report_names.__len__() - 1):
            report_name = report_names[i]
            self.driver.save_screenshot('../pictures/' + report_name + '.png')
            reports.reports.find_report(driver, report_name)
            reports.reports.go_to_report_CS(driver, report_name)
            reports.reports.add_filters_besides_default_ones(driver)
            reports.reports.view_report(driver)
            reports.reports.switch_to_report_view_page(driver, report_name, report_case_num[i])
            reports.reports.close_report_view_window(driver)
            reports.reports.close_report_cs_page(driver)

    def tearDown(self):
        # filename = time.time().__str__()+'teardown'
        filename = 'teardown'
        self.driver.save_screenshot('../pictures/'+filename+'.png')





if __name__ == '__main__':
    unittest.main()
