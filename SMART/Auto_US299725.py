import unittest
import SMART.Smart_commons as SC
from selenium import webdriver
import SMART.IP_report_page as IP_report
import SMART.Smart_com_acts as ACT




class MyTestCase(unittest.TestCase):



 def test_navigate_ip_report_cs(self):
    driver = webdriver.Firefox()

    reports_dic_enterprise = SC.read_file_as_list_report_US299725('enterprise')
    reports_dic_standard = SC.read_file_as_list_report_US299725('standard')

    reports_values = list(reports_dic_standard.values())
    reports_keys = list(reports_dic_standard.keys())

    SC.login_(driver)
    # go to report search page
    # IP_report.go_to_report_ip_Enterprise(driver)
    IP_report.go_to_report_ip_Standard(driver)

    for i in range(0, reports_values.__len__()-1):

       report = reports_values[i]

       # find "report name"
       try:
          IP_report.find_report_ip(driver, report)
       except:
          print('---try--except------'+report+'--not found-----')
          continue


       # click "report name"
       IP_report.go_to_report_CS(driver, report)

       # add filters besides the default ones
       IP_report.add_filters_besides_default_ones(driver,i)

       # operator

        #value
       # value_a = driver.find_element_by_xpath(
       #    './/div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[5]/div/div[4]/span/a')
       # value_a.click()
       #
       # ACT.wait_invisibility_of_element_located(driver)
       # ACT.wait_element_clickable(driver, By.XPATH,
       #                            '//div[@id="dvLookupuGrid"]/div[@class="k-grid-content"]/table/tbody/tr[1]')
       #
       # value_select_tr1 = driver.find_element_by_xpath(
       #    '//div[@id="dvLookupuGrid"]/div[@class="k-grid-content"]/table/tbody/tr[1]')
       # value_select_tr1.click()
       #
       # KEY.KeyboardKeys.keyDown(KEY.KeyboardKeys.VK_CODE['shift'])
       #
       # value_select_last = driver.find_element_by_xpath(
       #    '//div[@id="dvLookupuGrid"]/div[@class="k-grid-content"]/table/tbody/tr[last()]')
       # value_select_last.click()



       #operator_dropdown = driver.find_elements_by_xpath('//div[@class="k-animation-container"][1]/div/ul/li')

       # Click "View report"
       IP_report.view_report_by_default_filters(driver)
       # Go to report view page
       IP_report.swiitch_to_report_view_page(driver, report, reports_keys[i])
       # Export report
       # IP_report.export_report(driver, report)
       handles = driver.window_handles
       driver.close()
       driver.switch_to.window(handles[0])

       ACT.wait_invisibility_of_element_located(driver)
       close = driver.find_element_by_xpath('//span[text()="close"]')
       close.click()


 def test_US299725_enterprise(self):

      driver = webdriver.Firefox()
      reports_dic_enterprise = SC.read_file_as_list_report_US299725('enterprise')
      reports_values = list(reports_dic_enterprise.values())
      reports_keys = list(reports_dic_enterprise.keys())

      SC.login_(driver)
      # go to report search page
      # IP_report.go_to_report_ip_Enterprise(driver)
      IP_report.go_to_report_ip_Enterprise(driver)

      for i in range(0, reports_dic_enterprise.__len__()):

         report = reports_values[i]

         # find "report name"
         try:
            IP_report.find_report_ip(driver, report)
         except:
            print('---try--except------' + report + '--not found-----')


         # click "report name"
         IP_report.go_to_report_CS(driver, report)

         # add filters besides the default ones
         IP_report.add_filters_besides_default_ones(driver,i)

         # Click "View report"
         IP_report.view_report_by_default_filters(driver)
         # Go to report view page
         IP_report.swiitch_to_report_view_page(driver, report, reports_keys[i])
         # Export report
         # IP_report.export_report(driver, report)
         handles = driver.window_handles
         driver.close()
         driver.switch_to.window(handles[0])

         ACT.wait_invisibility_of_element_located(driver)
         close = driver.find_element_by_xpath('//span[text()="close"]')
         close.click()

 def tearDown(self):
    print('tearDown')
    # take a screnshot
    # print('---------take a screnshot-------------')
    # test_case_number = 'TC ' + str(report_case) + '-' + report
    # picture_path = 'pictures/' + report + '.png'
    # SC.file_exists_delete(picture_path)
    # picture = driver.save_screenshot(picture_path)
    # SC.write_test_result_as_docx(picture_path, test_case_number)
    # self.widget.dispose()

 if __name__ == '__main__':
    unittest.main()
