from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import SMART.Smart_common_settings as settings


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


def wait_for_login(driver):
    try:
        element = WebDriverWait(driver, settings.login_sleep).until(
            EC.presence_of_element_located((By.ID, "spUserName"))
        )
    finally:
     print('-----wait_for_login------')


def wait_presence_element(driver, located_by):
    try:
        element = WebDriverWait(driver, settings.sleep).until(
            EC.presence_of_element_located((By.ID,located_by))
        )
    finally:
        print('-----wait_presence_element------')