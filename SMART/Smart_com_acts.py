from selenium import webdriver
import SMART.Smart_com_report_names as re_name
def find_report_ip(self, driver, report_name):
    txtSearch_report = driver.find_element_by_id('txtSearch')
    txtSearch_report.clear()
    txtSearch_report.click()
    txtSearch_report.send_keys(report_name)

    spnSearch_report = driver.find_element_by_id('spnSearch')
    spnSearch_report.click()

def report_result_find_text(self, report_name):
    driver = webdriver.Firefox()
    driver.find_element_by_xpath("//br[text()="+report_name+"]")
