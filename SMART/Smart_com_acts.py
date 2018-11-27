from selenium import webdriver
import SMART.Smart_com_report_names as re_name
def find_report_ip(self, driver):
    txtSearch_report = driver.find_element_by_id('txtSearch')
    txtSearch_report.clear()
    txtSearch_report.click()
    txtSearch_report.send_keys(re_name.Case_Listing)

    spnSearch_report = driver.find_element_by_id('spnSearch')
    spnSearch_report.click()
