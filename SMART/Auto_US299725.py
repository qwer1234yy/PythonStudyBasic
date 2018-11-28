import unittest,SMART.Smart_urls as url
import SMART.Smart_commons as SC
import SMART.Smart_com_acts as act
from selenium import webdriver
import SMART.IP_report_page as IP_report
import SMART.Smart_com_report_names as IP_report_name
import SMART.inpatient_page as inPat
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

 def test_navigate_IPreport_CS(self):
    driver = webdriver.Firefox()
    SC.login_(self, driver)
    inPat.go_to_report_ip_Enterprise(self,driver)
    act.find_report_ip(self,driver,IP_report_name.Case_Mix_Index_CMI_Analysis)
    IP_report.go_to_report_CS(self,driver,IP_report_name.Case_Mix_Index_CMI_Analysis)
    driver.find_element_by_id()


 if __name__ == '__main__':
    unittest.main()
