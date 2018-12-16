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

        field_list = []
        field_dic = {}


        driver = self.driver
        SC.login_(driver)
        reports.reports.go_to_op_standard(driver)

        report_name = 'Visits Processed on Import'

        reports.reports.find_report(driver, report_name)
        reports.reports.go_to_report_CS(driver, report_name)

        # reports.reports.add_filters_besides_default_ones(driver)
        # set up filters
        ACT.wait_element_clickable(driver, By.ID, 'btnInsertClause')
        add_icon = driver.find_element_by_id('btnInsertClause')
        add_icon.click()
        driver.find_element_by_id('customsearch-grid-div')
        field_last = driver.find_element_by_xpath(
            './/div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[3]/span')
        field_last.click()

        # cycle all the options under field dropdown
        field_names_xpath = '//div[@class="k-animation-container"][last()]/div/ul/li'
        field_names = driver.find_elements_by_xpath(field_names_xpath)
        print('----------------------------------------------------')
        field_values = []
        for item in field_names:
            print(item.text)
            field_values.append(item.text)


        print('----------------------------------------------------')
        for i in range(0,len(field_values)):
            print('----------------------------------------------------')
            print(i)
            tools.spide_write_to_txt(field_values[i], '../Smart_commons/cs_fields.txt')
            print(field_values[i])
            field_dic['id'] = field_values[i]

            if i == 0:
                print(i)
            else:
                driver.find_element_by_id('customsearch-grid-div')
                field_last = driver.find_element_by_xpath(
                    '//div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[3]/span')
                field_last.click()

            field_name = field_values[i]
            field_names_xpath = '//div[@class="k-animation-container"][last()]/div/ul/li'
            field_names = driver.find_elements_by_xpath(field_names_xpath)

            for i in field_names:
                print(i.text)

            field_xpath = '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + field_name + '"]'
            print(field_xpath)
            ACT.wait_presence_element_xpath(driver, field_xpath)
            ACT.wait_element_clickable(driver, By.XPATH, field_xpath)
            field_name_select = driver.find_element_by_xpath(field_xpath)
            field_name_select.click()

            print('------click----field_name-----------'+field_name)

            # operator
            # click "operator" button
            operator = driver.find_element_by_xpath(
                '//div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[4]/span')
            operator.click()
            # cycle all the options under ope dropdown
            operator_names_xpath = '//div[@class="k-animation-container"][last()]/div/ul/li'
            operator_names = driver.find_elements_by_xpath(operator_names_xpath)

            operator_names[1].click()
            operators = ''
            for item in operator_names:
                tools.spide_write_to_txt(item.text, '../Smart_commons/cs_operators.txt')
                operators=operators+item.text+','
                print(item.text)
            field_dic['operators']=operators


            # click 'value' field
            xpath = './/div[@id="customsearch-grid"]/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[5]/div/div[6]/input'
            value_input = driver.find_element_by_xpath(xpath)
            value_input_property = value_input.get_property('disabled')
            print('----value_input_style-------')
            print(value_input_property)
            field_dic['type'] = 'input'
            field_dic['default'] = 'default'

            field_list.append(field_dic)
        tools.write_dics_list_to_xml('Fields', 'Field', field_list, '../Smart_commons/cs_fields.xml')
        for i in field_list:
            print(i)




if __name__ == '__main__':
    unittest.main()
