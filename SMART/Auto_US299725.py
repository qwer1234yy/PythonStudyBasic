import unittest
import SMART.Smart_commons as SC
from selenium import webdriver
import SMART.IP_report_page as IP_report
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import SMART.Smart_common_settings as settings
import SMART.Smart_com_acts as ACT



class MyTestCase(unittest.TestCase):

 def test_navigate_ip_report_cs(self):
    driver = webdriver.Firefox()
    reports = SC.read_file_as_list('reports_names.txt')
    SC.login_(driver)
    # go to report search page
    # IP_report.go_to_report_ip_Enterprise(driver)
    IP_report.go_to_report_ip_Standard(driver)

    for report in reports:

       # find "report name"
       IP_report.find_report_ip(driver, report)
       # click "report name"
       IP_report.go_to_report_CS(driver, report)

       # add filters besides the default ones
       IP_report.add_filters_besides_default_ones(driver)

       # Click "View report"
       IP_report.view_report_by_default_filters(driver)
       # Go to report view page
       IP_report.swiitch_to_report_view_page(driver, report)
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
