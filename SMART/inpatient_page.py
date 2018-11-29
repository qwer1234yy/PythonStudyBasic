import time,SMART.Smart_common_settings as settings
import SMART.Smart_com_acts as ACT
from selenium.webdriver.common.by import By



def go_to_report_ip_Enterprise(self,driver):

    # Click "inpatient"
    inpatient = driver.find_element_by_id('aModuleSIP101')
    time.sleep(10)
    inpatient.click()

    # Click "report"
    report = driver.find_element_by_id('aIPModuleWorkplans')
    report.click()
    time.sleep(10)

    # Click "Inpatient Enterprise Reports"
    enterprice_link = driver.find_element_by_xpath('//span[text()="Inpatient Enterprise Reports"]')
    enterprice_link.click()
    # wait
    spnSearch = driver.find_element_by_id('spnSearch')
    ACT.wait_presence_element(driver,'spnSearch')


def go_to_report_ip_Standard(self,driver):
    # Click "inpatient"
    inpatient = driver.find_element_by_id('aModuleSIP101')
    time.sleep(10)
    inpatient.click()
    # inpatient.send_keys(Keys.ENTER)

    # Click "report"
    report = driver.find_element_by_id('aIPModuleWorkplans')
    report.click()
    time.sleep(10)

    # Click "Inpatient Standard Reports"
    enterprice_link = driver.find_element_by_xpath('//span[text()="Inpatient Standard Reports"]')
    enterprice_link.click()
    time.sleep(settings.sleep)