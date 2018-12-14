import unittest,time
from selenium import webdriver
import SMART.Smart_commons as SC
import SMART.Smart_com_acts as ACT
from selenium.webdriver.common.by import By
import SMART.Smart_reports as reports
import SMART.Smart_base_driver as drivers
import SMART.Smart_tools.tools as tools


class MyTestCase(unittest.TestCase):

    driver = drivers.driver_firefox()

    def setUp(self):

        print('setup')

    def test_enterprise_reports(self):

        reports_name_cases = SC.read_file_report_names_as_list('enterprise')
        report_names = []
        report_case_num = []
        for i in reports_name_cases:
            report_names.append(reports_name_cases[i])
            report_case_num.append(i)
        driver = self.driver
        SC.login_(driver)
        reports.reports.go_to_op_enterprise(driver)

        report_name = 'Visits Processed on Import'

        reports.reports.find_report(driver, report_name)
        reports.reports.go_to_report_CS(driver, report_name)




        # reports.reports.add_filters_besides_default_ones(driver)
        # set up filters
        ACT.wait_element_clickable(driver, By.ID, 'btnInsertClause')

        add_icon = driver.find_element_by_id('btnInsertClause')
        add_icon.click()

        # add filters besides the default ones
        # click 'Field' dropdown
        driver.find_element_by_id('customsearch-grid-div')
        field_last = driver.find_element_by_xpath(
            './/div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[3]/span')
        field_last.click()

        # fields_lis = driver.find_elements_by_xpath('//div[@class="k-animation-container"][last()]/div/ul/li')
        # print(fields_lis.__len__())
        # for li in fields_lis:
        #     print(li.text)

        # cycle all the options under field dropdown
        field_names_xpath = '//div[@class="k-animation-container"][last()]/div/ul/li'
        field_names = driver.find_elements_by_xpath(field_names_xpath)
        for item in field_names:
            print(item.text)

        # select a field
        field_name = 'ICD Dx Codes - Admit'
        field_xpath = '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + field_name + '"]'
        print(field_xpath)
        ACT.wait_presence_element_xpath(driver, field_xpath)
        ACT.wait_element_clickable(driver, By.XPATH, field_xpath)
        field_name_select = driver.find_element_by_xpath(field_xpath)
        field_name_select.click()
        print('----------field_name-----------')
        print(field_name)

        # operator

        # click "operator" button
        operator = driver.find_element_by_xpath(
            '//div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[4]/span')
        operator.click()

        # cycle all the options under ope dropdown
        operator_names_xpath = '//div[@class="k-animation-container"][last()]/div/ul/li'
        operator_names = driver.find_elements_by_xpath(operator_names_xpath)
        for item in field_names:
            tools.spide_write_to_txt(item.text, '../Smart_commons/cs_operators.txt')
            print(item.text)

        # select operator_value  < Less Than In
        operator_value = '<> Not Equal'
        ACT.wait_presence_element_xpath(driver,
                                        '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + operator_value + '"]')
        operator_in = driver.find_element_by_xpath(
            '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + operator_value + '"]')
        operator_in.click()

        # click 'value' field
        xpath = './/div[@id="customsearch-grid"]/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[5]/div/div[6]/input'
        value_input = driver.find_element_by_xpath(xpath)
        value_input.click()
        value_input.send_keys('434.91')
        print('-------send_keys---------Z12.11--434.91-----')




if __name__ == '__main__':
    unittest.main()
