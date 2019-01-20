import unittest,time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        screenshot_name = "exception.png"
        driver.get_screenshot_as_file(screenshot_name)
        print("Screenshot saved as '%s'" % screenshot_name)

class TestDemo(unittest.TestCase):
    def test_demo(self):

        firfox_driver = webdriver.Firefox()
        driver = EventFiringWebDriver(firfox_driver, ScreenshotListener())

        driver.get("http://strzw058080/SMARTSolutions/")
        login_ele = driver.find_element_by_id('txtLoginid')
        password_ele = driver.find_element_by_id('txtPassword')
        login_ele_btn = driver.find_element_by_id('btnloginText')

        login_ele.clear()
        login_ele.send_keys('admin')

        password_ele.clear()
        password_ele.send_keys('Admin')
        login_ele_btn.click()

        time.sleep(10)
        WebDriverWait(driver, 300).until(
            EC.element_to_be_clickable((By.ID, 'aSlideMenuSelModuleSIP101')))

        print(driver.page_source)

        driver.find_element_by_id('aSlideMenuSelModuleSIP101').click()

if __name__ == '__main__':
        unittest.main()