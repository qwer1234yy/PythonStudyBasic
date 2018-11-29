import SMART.Smart_urls as base_url
import time
import SMART.Smart_common_settings as S_set
import SMART.Smart_com_acts as Act


def login_(driver):

    driver.get(base_url.base_url)

    login_ele = driver.find_element_by_id('txtLoginid')
    password_ele = driver.find_element_by_id('txtPassword')
    login_ele_btn = driver.find_element_by_id('btnloginText')

    login_ele.clear()
    login_ele.send_keys('admin')
    password_ele.clear()
    password_ele.send_keys('Admin')
    login_ele_btn.click()
    # wait for login completed
    Act.wait_for_login(driver)


def navigate_to_ip_report_enterprise(self,driver):
    # navigate to IP report search page
    driver.get(base_url.ip_report_url)
    time.sleep(S_set.sleep)
    # click "Inpatient Enterprise Reports" link
    enterprice_link = driver.find_element_by_id('aWorkplanLink')
    enterprice_link.click()
    time.sleep(S_set.sleep)


def navigate_to_ip_report_standard(self,driver):
    # navigate to IP report search page
    driver.get(base_url.ip_report_url)
    time.sleep(S_set.sleep)
    # click "Inpatient Enterprise Reports" link
    standard_link = driver.find_element_by_id('aWorkplanNameMS')
    standard_link.click()
    time.sleep(S_set)

