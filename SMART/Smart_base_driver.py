import unittest,os,time
import SMART.Smart_commons as SC
from selenium import webdriver
import SMART.IP_report_page as IP_report
import SMART.Smart_com_acts as ACT
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.options import Options as IEoptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class driver(object):

    def chrome_driver(self):

        capabilities = {
            'browserName': 'chrome',
            'chromeOptions': {
                'useAutomationExtension': False,
                'forceDevToolsScreenshot': True,
                'args': ['--disable-infobars']
                # 'args': ['--start-maximized', '--disable-infobars']
            }
        }
        drive = webdriver.Chrome(desired_capabilities=capabilities)
        return drive


def driver_chrome():

    capabilities = {
        'browserName': 'chrome',
        'chromeOptions': {
            'useAutomationExtension': False,
            'forceDevToolsScreenshot': True,
            'args': ['--disable-infobars']
            # 'args': ['--start-maximized', '--disable-infobars']
        }
    }
    drive = webdriver.Chrome(desired_capabilities=capabilities)
    return drive


def driver_firefox():
    drive = webdriver.Firefox()
    drive.maximize_window()
    return drive