import unittest
from selenium.webdriver import Firefox
from SMART import Smart_commons
from SMART.Smart_pages import Smart_reports


class MyTestCase(unittest.TestCase):

    driver = ''
    def setUp(self):
        self.driver = Firefox()

    def test_get_report_names(self):

        Smart_commons.login_(self.driver)
        Smart_reports.reports.go_to_op_enterprise(self.driver)

        #
        reports_tree = self.driver.find_elements_by_xpath()



if __name__ == '__main__':
    unittest.main()
