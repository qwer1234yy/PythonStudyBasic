import unittest,os,time
import SMART.Smart_commons as SC
from selenium import webdriver
import SMART.IP_report_page as IP_report
import SMART.Smart_com_acts as ACT
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.options import Options as IEoptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class MyTestCase(unittest.TestCase):
    def test_grab_(self):
        url = 'http://strzw058059/SMARTSolutions/Inpatient/ReferenceGuides'
        driver = webdriver.Firefox()
        SC.login_(driver)
        driver.get(url)
        ACT.wait_document_completed(driver)
        Tables_for_FY17_links_xpath_li = '//dic[@id="dvDrgTypeGridBody"]/div/ul/li'

        Tables_for_FY17_links = driver.find_elements_by_xpath(Tables_for_FY17_links_xpath_li)
        print('----------------------')
        for li in range(1,Tables_for_FY17_links.__sizeof__()):

            Tables_for_FY17_links_xpath_li_a_href = '//dic[@id="dvReferenceTypeListBody"]/div/ul/li[' + li.__str__() + ']/a'
            Tables_for_FY17_links_text = '//dic[@id="dvReferenceTypeListBody"]/div/ul/li[' + li.__str__() + ']/a/div'

            href_a = driver.find_element_by_xpath(Tables_for_FY17_links_xpath_li_a_href)
            text_div = driver.find_element_by_xpath(Tables_for_FY17_links_text)
            print(href_a.get_property('href'))
            print(text_div.text)


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest('test_grab11_')
