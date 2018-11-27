import unittest,SMART.Smart_urls as url
import SMART.Smart_commons as SC
import SMART.Smart_com_acts as act
from selenium import webdriver
import SMART.IP_report_page as IP_report
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

 def test_navigate_IPreport(self):
    driver = webdriver.Firefox()
    SC.login_(self, driver)
    SC.navigate_to_ip_report_enterprise(self,driver)
    act.find_report_ip(self,driver)
    IP_report.go_to_report(self,driver,'Case Listing')

 if __name__ == '__main__':
    unittest.main()
