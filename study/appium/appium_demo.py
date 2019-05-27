import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def test_something(self):
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)
        # driver = webdriver.webdriver.WebDriver(desired_capabilities=desired_caps)
        driver.find_element_by_name("Clear").click()
        driver.find_element_by_name("Seven").click()
        driver.find_element_by_name("Clear").click()

        driver.quit()


if __name__ == '__main__':
    unittest.main()
