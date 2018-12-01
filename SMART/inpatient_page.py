import time,SMART.Smart_common_settings as settings
import SMART.Smart_com_acts as ACT
from selenium.webdriver.common.by import By



def go_to_report_ip_Enterprise(self,driver):

    # Click "inpatient"
    inpatient = driver.find_element_by_id('aModuleSIP101')
    inpatient.click()

    # Click "report"
    report = driver.find_element_by_id('aIPModuleWorkplans')
    report.click()
    ACT.wait_presence_element_xpath(driver,'//span[text()="Inpatient Enterprise Reports"]')

    # Click "Inpatient Enterprise Reports"
    enterprice_link = driver.find_element_by_xpath('//span[text()="Inpatient Enterprise Reports"]')
    enterprice_link.click()
    # wait
    ACT.wait_presence_element(driver,'txtSearch')


def go_to_report_ip_Standard(self,driver):
    # Click "inpatient"
    inpatient = driver.find_element_by_id('aModuleSIP101')
    inpatient.click()

    # Click "report"
    report = driver.find_element_by_id('aIPModuleWorkplans')
    report.click()

    # Click "Inpatient Standard Reports"
    enterprice_link = driver.find_element_by_xpath('//span[text()="Inpatient Standard Reports"]')
    enterprice_link.click()


def find_report_ip(self, driver, report_name):

    #ACT.wait_presence_element(driver,'spnSearch')
    #ACT.wait_invisibility_of_element_located(driver)

    ACT.wait_modal_overlay_element(driver, By.ID, 'spnSearch')

    txtSearch_report = driver.find_element_by_id('txtSearch')
    txtSearch_report.clear()
    txtSearch_report.click()
    txtSearch_report.send_keys(report_name)

    spnSearch_report = driver.find_element_by_id('spnSearch')
    spnSearch_report.click()


def report_result_find_text(driver,report_name):
    driver.find_element_by_xpath("//br[text()="+report_name+"]")
