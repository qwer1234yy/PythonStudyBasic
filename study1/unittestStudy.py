import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.testcase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        time.sleep(3)
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_id("id-search-field")
        # elem = driver.find_element_by_name("q")
        elem.send_keys("Python")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_baidu(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        time.sleep(3)
        self.assertIn("百度一下", driver.title)
        # search_elem = driver.find_element_by_id("kw")
        search_elem = driver.find_element_by_class_name("s_ipt")
        print(search_elem)
        print("search_elem")
        search_elem.send_keys("Python")
        search_elem.send_keys(Keys.RETURN)
        assert "Welcome to Python.org" not in driver.page_source
        print("Welcome to Python.org" not in driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
