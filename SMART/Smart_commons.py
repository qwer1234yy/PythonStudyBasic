from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SMART.Smart_urls as base_url
import time
import SMART.Smart_common_settings as S_set

def login(self):
    driver = webdriver.Firefox()
    driver.get(base_url.base_url)

    login_ele = driver.find_element_by_id('txtLoginid')
    password_ele = driver.find_element_by_id('txtPassword')
    login_ele_btn = driver.find_element_by_id('btnloginText')

    login_ele.clear()
    login_ele.send_keys('admin')
    password_ele.clear()
    password_ele.send_keys('Admin')
    login_ele_btn.click()

    try:
        element = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.ID, "spUserName"))
        )
        print('wait')
    finally:
        print(driver.current_url)
def login_(self,driver):

    driver.get(base_url.base_url)

    login_ele = driver.find_element_by_id('txtLoginid')
    password_ele = driver.find_element_by_id('txtPassword')
    login_ele_btn = driver.find_element_by_id('btnloginText')

    login_ele.clear()
    login_ele.send_keys('admin')
    password_ele.clear()
    password_ele.send_keys('Admin')
    login_ele_btn.click()

    try:
        element = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.ID, "spUserName"))
        )
        print('wait')
    finally:
        print(driver.current_url)

def wait(self, element,driver):

    try:
        element_final = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located(element)
        )
        print('wait')
    finally:
        print(driver.current_url)
def navigate_to_ip_report_enterprise(self,driver):
    #navigate to IP report search page
    driver.get(base_url.ip_report_url)
    time.sleep(S_set.sleep)
    #click "Inpatient Enterprise Reports" link
    enterprice_link = driver.find_element_by_id('aWorkplanLink')
    enterprice_link.click()
    time.sleep(S_set.sleep)


def navigate_to_ip_report_standard(self,driver):
    #navigate to IP report search page
    driver.get(base_url.ip_report_url)
    time.sleep(S_set.sleep)
    #click "Inpatient Enterprise Reports" link
    standard_link = driver.find_element_by_id('aWorkplanNameMS')
    standard_link.click()
    time.sleep(S_set)

