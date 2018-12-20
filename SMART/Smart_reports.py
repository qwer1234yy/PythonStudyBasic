from selenium.webdriver.common.action_chains import ActionChains
import SMART.Smart_com_acts as ACT
from selenium.webdriver.common.by import By
import time, os
from pykeyboard import PyKeyboard
import SMART.Smart_commons as SC
import SMART.Smart_tools.tools as tools


class reports(object):

 def go_to_report_ip_Standard(driver):
    # Click "inpatient"
    ACT.wait_element_clickable(driver, By.ID, 'aModuleSIP101')
    ACT.wait_invisibility_of_element_located(driver)
    inpatient = driver.find_element_by_id('aModuleSIP101')
    inpatient.click()

    # Click "report"
    report = driver.find_element_by_id('aIPModuleWorkplans')
    report.click()
    ACT.wait_presence_element_xpath(driver, '//span[text()="Inpatient Standard Reports"]')

    # Click "Inpatient Standard Reports"
    standard_link = driver.find_element_by_xpath('//span[text()="Inpatient Standard Reports"]')
    standard_link.click()
    # wait
    ACT.wait_invisibility_of_element_located(driver)

 def go_to_op_enterprise(driver):
     # click "Outpatient"
     ACT.wait_element_clickable(driver, By.ID, 'aSlideMenuSelModuleOP101')
     outpatient_enter = driver.find_element_by_id('aSlideMenuSelModuleOP101')
     ACT.wait_invisibility_of_element_located(driver)
     outpatient_enter.click()

     # click "Reports"
     ACT.wait_element_clickable(driver, By.ID, 'aOPModuleWorkplans')
     OP_report_enter = driver.find_element_by_id('aOPModuleWorkplans')
     OP_report_enter.click()


     # Click "Inpatient Enterprise Reports"
     xpath = '//span[text()="Outpatient Enterprise Reports"]'
     ACT.wait_element_clickable(driver, By.XPATH, xpath)
     enterprice_link = driver.find_element_by_xpath(xpath)
     enterprice_link.click()
     # wait
     ACT.wait_invisibility_of_element_located(driver)
 def go_to_op_standard(driver):
     # click "Outpatient"
     ACT.wait_element_clickable(driver, By.ID, 'aSlideMenuSelModuleOP101')
     outpatient_enter = driver.find_element_by_id('aSlideMenuSelModuleOP101')
     ACT.wait_invisibility_of_element_located(driver)
     outpatient_enter.click()

     # click "Reports"
     ACT.wait_element_clickable(driver, By.ID, 'aOPModuleWorkplans')
     OP_report_enter = driver.find_element_by_id('aOPModuleWorkplans')
     OP_report_enter.click()

     # Click "Outpatient Standard Reports"
     xpath = '//span[text()="Outpatient Standard Reports"]'
     ACT.wait_element_clickable(driver, By.XPATH, xpath)
     enterprice_link = driver.find_element_by_xpath(xpath)
     enterprice_link.click()
     # wait
     ACT.wait_invisibility_of_element_located(driver)

 def find_report(driver, report_name):

     ACT.wait_presence_element(driver, 'spnSearch')
     # ACT.wait_invisibility_of_element_located(driver)

     ACT.wait_modal_overlay_element(driver, By.ID, 'txtSearch')
     txtSearch_report = driver.find_element_by_id('txtSearch')

     ACT.wait_element_clickable(driver, By.ID, 'txtSearch')
     ACT.wait_presence_element(driver, 'txtSearch')
     time.sleep(5)
     txtSearch_report.clear()
     txtSearch_report.click()
     txtSearch_report.send_keys(report_name)

     spnSearch_report = driver.find_element_by_id('spnSearch')
     spnSearch_report.click()
     ACT.wait_element_clickable(driver, By.PARTIAL_LINK_TEXT, report_name)
     time.sleep(1)

 def go_to_report_CS(driver, report_name):

     if report_name == 'Frequency':

         # Case_Listing_link = driver.find_elements_by_link_text(report_name)[1]
         # Case_Listing_links = driver.find_elements_by_xpath("//a[text()="+report_name+"]")
         # print(len(Case_Listing_links))
         # Case_Listing_link = Case_Listing_links[1]
         Case_Listing_link = driver.find_elements_by_partial_link_text(report_name)[3]
     else:
         Case_Listing_link = driver.find_element_by_partial_link_text(report_name)

     print('---go_to_report_CS---double_click------')
     ActionChains(driver).double_click(Case_Listing_link).perform()
     ACT.wait_invisibility_of_element_located(driver)
     ACT.wait_presence_element(driver, 'btnViewReport')
     ACT.wait_element_clickable(driver, By.ID, 'btnViewReport')
     time.sleep(5)
 def add_filters_besides_default_ones(driver):

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

    #operator


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
    ACT.wait_presence_element_xpath(driver, '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + operator_value + '"]')
    operator_in = driver.find_element_by_xpath(
        '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + operator_value + '"]')
    operator_in.click()

    # click 'value' field
    xpath = './/div[@id="customsearch-grid"]/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[5]/div/div[6]/input'
    value_input = driver.find_element_by_xpath(xpath)
    value_input.click()
    value_input.send_keys('434.91')
    print('-------send_keysTest---------Z12.11--434.91-----')

 def view_report(driver):
     # click 'View Report' button
     btnViewReport = driver.find_element_by_id('btnViewReport')
     ACT.wait_element_clickable(driver, By.ID, 'btnViewReport')
     ACT.wait_invisibility_of_element_located(driver)
     btnViewReport.click()
     ACT.wait_invisibility_of_element_located(driver)
     time.sleep(1)
     print('--------view_report_by_default_filters------------')

 def switch_to_report_view_page(driver, report_name, report_case):

     view_report_window = driver.window_handles[1]
     driver.switch_to.window(view_report_window)
     print('------window1------' + report_name)
     if report_name == 'DRG Change Condition Detail':
         ACT.wait_until_title_contains(driver, 'DRG Change Detail')
     elif report_name == 'Top 50 Diagnoses by Present on Admission(POA)':
         ACT.wait_until_title_contains(driver, 'Top 50 Other Diagnoses by Present on Admission(POA)')
     elif report_name == 'Management Clinical Profile':
         ACT.wait_until_title_contains(driver, 'Evaluation')
     elif 'Frequency' in report_name:
         ACT.wait_until_title_contains(driver, 'Frequency')
     else:
         ACT.wait_until_title_contains(driver, report_name)
     print(view_report_window)
     print(driver.title)
     print('---wait_presence_element--------RW_ReportToolbar_ExportGr_FormatList_DropDownList----------')
     print('-----driver.execute_script(document.redyState)--------')
     print(driver.execute_script('return document.readyState'))
     # wait report load fully
     ACT.wait_document_completed(driver)

     # take a screnshot
     print('---------take a screnshot-------------')
     SC.screen_shot_report_us_test_result(driver, report_name, report_case)

     print('switch_to_report_view_page'+report_name+'---------end')

 def close_report_view_window(driver):
     handles = driver.window_handles
     driver.close()
     driver.switch_to.window(handles[0])
     ACT.wait_invisibility_of_element_located(driver)

 def close_report_cs_page(driver):
     close = driver.find_element_by_xpath('//span[text()="close"]')
     close.click()
