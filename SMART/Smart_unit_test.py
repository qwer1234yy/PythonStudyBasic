import unittest,time
import SMART.Smart_commons as SC
from selenium import webdriver
import SMART.Smart_com_acts as ACT


class MyTestCase(unittest.TestCase):
    def test_wait(self):
        driver = webdriver.Firefox()
        SC.login_(driver)

        # Click "inpatient"
        inpatient = driver.find_element_by_id('aModuleSIP101')
        inpatient.click()

        # Click "report"
        report = driver.find_element_by_id('aIPModuleWorkplans')
        report.click()

    def test_txt(self):
        fields_f = open('custom_search_fields.txt','r')
        lines = fields_f.readlines()
        fields = []
        print(lines.__len__())
        for line in lines:
             print(line.strip())
             fields.append(line.strip())
        fields_f.close()

    def test_get_default_fields(self):
        print('test_get_default_fields')

    def test_read_as_list(self):
        # custom_search_fields.txt
        items = SC.read_file_as_list('reports_names.txt')

        for item in items:
            print(item)


if __name__ == '__main__':
    unittest.main()
