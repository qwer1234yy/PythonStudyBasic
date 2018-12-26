from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import SMART.Smart_common_setings as settings
import SMART.Smart_settings.settings as sets
import time




def wait_for_login(driver):
    try:
        element = WebDriverWait(driver, settings.login_sleep).until(
            EC.presence_of_element_located((By.ID, "spUserName"))
        )
    finally:
     print('-----wait_for_login------')


def wait_document_completed(driver):

    for i in range(1, settings.sleep):
        print(i)
        print(driver.execute_script('return document.readyState'))
        if ('complete' == driver.execute_script('return document.readyState')):
            print(driver.execute_script('return document.readyState'))
            break
        else:
            time.sleep(1)

def wait_report_loaded(driver, report_name):

    responsed = False
    for i in range(1,sets.report_load_timeout):
        print(i)
        print(driver.execute_script('return document.readyState'))
        if('complete' == driver.execute_script('return document.readyState')):
            print(driver.execute_script('return document.readyState'))
            responsed = True
            break
        else:
            time.sleep(1)

    if responsed:
        pass
    else:
        print('report takes too long to response:'+report_name)
    return responsed


def wait_presence_element(driver, located_id):
    try:
        element = WebDriverWait(driver, settings.sleep).until(
            EC.presence_of_element_located((By.ID, located_id))
        )
    finally:
        print('-----wait_presence_element------')

def wait_element_clickable(driver, by_what, by_target):
    print('wait_element_clickable')
    try:
        element = WebDriverWait(driver, settings.sleep).until(
            EC.presence_of_element_located((by_what, by_target))
        )
    finally:
        print('-----wait_element_clickable------')


def wait_invisibility_of_element_located(driver):
    WebDriverWait(driver,settings.login_sleep).until(EC.invisibility_of_element_located((By.XPATH,"//div[@class='modalOverlay']")))

def wait_until_title_contains(driver, report):

    try:
        WebDriverWait(driver, settings.login_sleep).until(EC.title_contains(report))
    except:
        print('---try--except------' + report + '-title-not found--in view report page---')
        # continue


def wait_presence_element_xpath(driver, xpath):
    print('wait_presence_element_xpath----' + xpath)
    try:
        element = WebDriverWait(driver, settings.sleep).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    finally:
        print('-----wait_presence_element_xpath------')

def wait_presence_element_class(driver, class_):
    print('wait_presence_element_class----' + class_)
    try:
        element = WebDriverWait(driver, settings.sleep).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_))
        )
    finally:
        print('-----wait_presence_element_xpath------')


def wait_modal_overlay_element(driver, by_what, by_target):
    try:

        WebDriverWait(driver, settings.login_sleep).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='modalOverlay']")))

        WebDriverWait(driver, settings.sleep).until(
            EC.presence_of_element_located((by_what, by_target))
        )

    finally:
        print('-----wait_modalOverlay_element------')

def wait_new_window_is_opened(driver):
    try:
        WebDriverWait(driver, settings.sleep).until(
            EC.new_window_is_opened(driver.current_window_handle)
        )

    finally:
        print('-----wait_modalOverlay_element------')

    print('-------wait_new_window_is_opened-------------')