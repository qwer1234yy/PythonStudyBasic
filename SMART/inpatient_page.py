from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,SMART.Smart_common_settings as settings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def go_to_report_ip_Enterprise(self,driver):

    #Click "inpatient"
    inpatient = driver.find_element_by_id('aModuleSIP101')
    time.sleep(10)
    inpatient.click()

    # Click "report"
    report = driver.find_element_by_id('aIPModuleWorkplans')
    report.click()
    time.sleep(10)

    # Click "Inpatient Enterprise Reports"
    enterprice_link = driver.find_element_by_xpath('//span[text()="Inpatient Enterprise Reports"]')
    # enterprice_link = driver.find_element_by_id('aWorkplanNameMSShortName')
    enterprice_link.click()
    time.sleep(settings.sleep)


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