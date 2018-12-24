import unittest
import unittest,os,time
import SMART.Smart_commons as SC
from selenium import webdriver
import SMART.IP_report_page as IP_report
import SMART.Smart_com_acts as ACT
from selenium import webdriver
import SMART.Smart_reports as reports
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.options import Options as IEoptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class MyTestCase(unittest.TestCase):

    def test_something(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        enterprise_or_standard = 'enterprise' # enterprise standard
        reports_dic_standard = SC.read_file_report_names_as_list(enterprise_or_standard)
        reports_values = list(reports_dic_standard.values())
        reports_keys = list(reports_dic_standard.keys())

        SC.login_(driver)
        # go to report search page
        # IP_report.go_to_report_ip_Enterprise(driver)
        if 'standard' in enterprise_or_standard:
           # IP_report.go_to_report_ip_Standard(driver)
           reports.reports.go_to_op_standard(driver)
        else:
           # IP_report.go_to_report_ip_Enterprise(driver)
           reports.reports.go_to_op_enterprise(driver)

        for i in range(0, reports_dic_standard.__len__()):

            report = reports_values[i]
            # report = 'Frequency'
            # find "report name"
            try:
                IP_report.find_report_ip(driver, report)
            except:
                print('---try--except------' + report + '--not found-----')
                # continue

            # click "report name"
            IP_report.go_to_report_CS(driver, report)

            # add filters besides the default ones
            IP_report.add_filters_besides_default_ones(driver, i,report)

            # Click "View report"
            IP_report.view_report_by_default_filters(driver)
            # Go to report view page
            IP_report.swiitch_to_report_view_page(driver, report, reports_keys[i])
            # Export report
            # IP_report.export_report(driver, report)
            handles = driver.window_handles
            driver.close()
            driver.switch_to.window(handles[0])

            ACT.wait_invisibility_of_element_located(driver)
            close = driver.find_element_by_xpath('//span[text()="close"]')
            close.click()


if __name__ == '__main__':
    unittest.main()
