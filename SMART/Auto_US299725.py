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

 def test_US299725_IE11(self):

     # IE_path = r'C:\Program Files\Internet Explorer\ExtExport.exe'
     # os.environ['webdriver.ie.driver'] = IE_path
     # driver = webdriver.Ie(IE_path)

     caps = DesiredCapabilities.INTERNETEXPLORER

     caps = {
         'ignoreProtectedModeSettings': True,
         'ignore_protected_mode_settings': True,
         'ignore_zoom_level': True,
         'native_events': False,
         'persistent_hover': False,
         'ELEMENT_SCROLL_BEHAVIOR': True,
         'require_window_focus': True
     }

     opts = IEoptions()
     opts.ignore_protected_mode_settings = True
     opts.ignore_zoom_level = True
     opts.require_window_focus = True
     opts.native_events = False
     opts.ignore_protected_mode_settings = True
     opts.persistent_hover = False
     opts.ELEMENT_SCROLL_BEHAVIOR = True
     # opts.ensure_clean_session = True


     # ie_options=opts,executable_path=IE_path,
     driver = webdriver.Ie(options=opts)

     reports_dic_enterprise = SC.read_file_as_list_report_US299725('enterprise')
     reports_values = list(reports_dic_enterprise.values())
     reports_keys = list(reports_dic_enterprise.keys())
     SC.login_(driver)
     # go to report search page
     # IP_report.go_to_report_ip_Enterprise(driver)
     IP_report.go_to_report_ip_Enterprise(driver)

     for i in range(10, 19):

         report = reports_values[i]

         # find "report name"
         try:
             IP_report.find_report_ip(driver, report)
         except:
             print('---try--except------' + report + '--not found-----')

         # click "report name"
         IP_report.go_to_report_CS(driver, report)

         # add filters besides the default ones
         IP_report.add_filters_besides_default_ones(driver, i)

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

 def test_navigate_ip_report_cs_firefox(self):

     # profile = webdriver.FirefoxProfile()
     # profile.set_preference("network.proxy.type", 1)
     # profile.set_preference("network.proxy.http", "proxy.server.address")
     # profile.set_preference("network.proxy.http_port", "port_number")
     # profile.update_preferences()
     # driver = webdriver.Firefox(firefox_profile=profile)




     #activate a browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    reports_dic_standard = SC.read_file_as_list_report_US299725('standard')
    reports_values = list(reports_dic_standard.values())
    reports_keys = list(reports_dic_standard.keys())

    SC.login_(driver)
    # go to report search page
    # IP_report.go_to_report_ip_Enterprise(driver)
    IP_report.go_to_report_ip_Standard(driver)

    for i in range(0, reports_dic_standard.__len__()):

       report = reports_values[i]
       # report = 'Frequency'
       # find "report name"
       try:
          IP_report.find_report_ip(driver, report)
       except:
          print('---try--except------'+report+'--not found-----')
          # continue


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

 def test_US299725_enterprise_chrome(self):

      # executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
      # os.environ["webdriver.chrome.driver"] = executable_path
      # options = webdriver.ChromeOptions()
      # options.extensions.clear()
      # driver = webdriver.Chrome(chrome_options=options)
      # SC.login_(driver)
      # # go to report search page
      # # IP_report.go_to_report_ip_Enterprise(driver)
      # IP_report.go_to_report_ip_Enterprise(driver)

      # capabilities = {
      #     'browserName': 'chrome',
      #     'chromeOptions': {
      #         'useAutomationExtension': False,
      #         'forceDevToolsScreenshot': True,
      #         'args': ['--start-maximized', '--disable-infobars']
      #     }
      # }
      #
      # driver = webdriver.Chrome(desired_capabilities=capabilities)

      # SC.login_(driver)
      # go to report search page
      # IP_report.go_to_report_ip_Enterprise(driver)
      # IP_report.go_to_report_ip_Enterprise(driver)
      # driver.maximize_window()

      reports_dic_standard = SC.read_file_as_list_report_US299725('standard')
      reports_values = list(reports_dic_standard.values())
      reports_keys = list(reports_dic_standard.keys())

      # reports_dic_enterprise = SC.read_file_as_list_report_US299725('enterprise')
      # reports_values = list(reports_dic_enterprise.values())
      # reports_keys = list(reports_dic_enterprise.keys())



      ones = reports_dic_standard.__len__()
      for i in range(0, ones):
         # executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
         # os.environ["webdriver.chrome.driver"] = executable_path
         # options = webdriver.ChromeOptions()
         # options.extensions.clear()


         # driver = webdriver.Chrome(chrome_options=options)

         capabilities = {
             'browserName': 'chrome',
             'chromeOptions': {
                 'useAutomationExtension': False,
                 'forceDevToolsScreenshot': True,
                 'args': ['--disable-infobars']
                 # 'args': ['--start-maximized', '--disable-infobars']
             }
         }
         driver = webdriver.Chrome(desired_capabilities=capabilities)
         SC.login_(driver)
         # go to report search page
         IP_report.go_to_report_ip_Standard(driver)
         # IP_report.go_to_report_ip_Enterprise(driver)

         report = reports_values[i]
         report = 'Medicare HAC Potential Impact'
         # report = 'Frequency'
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
         # handles = driver.window_handles
         # print(handles.__len__())
         # for handle in driver.window_handles:
         #     print(handle)
         #     print('-------window_handles------------------')
         # print(driver.current_window_handle)
         # driver.switch_to.window(driver.current_window_handle)
         # time.sleep(10)
         #
         # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'W')
         #
         # print('--------------Keys.CONTROL+w--------------')


         # time.sleep(5)
         # driver.switch_to.window(driver.current_window_handle)
         # driver.close()
         driver.quit()
         # print(handles[0])
         # print(handles[1])
         # driver.switch_to.window(driver.window_handles[0])

         # ACT.wait_invisibility_of_element_located(driver)
         # close = driver.find_element_by_xpath('//span[text()="close"]')
         # close.click()



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
