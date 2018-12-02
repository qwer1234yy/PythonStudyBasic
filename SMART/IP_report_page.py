from selenium.webdriver.common.action_chains import ActionChains
import SMART.Smart_com_acts as ACT
from selenium.webdriver.common.by import By
import time
from pykeyboard import PyKeyboard
from pymouse import *


#click and enter a report
def go_to_report_CS(driver, report_name):

    Case_Listing_link = driver.find_element_by_link_text(report_name)
    print('---go_to_report_CS---double_click------')
    ActionChains(driver).double_click(Case_Listing_link).perform()
    ACT.wait_invisibility_of_element_located(driver)
    ACT.wait_presence_element(driver, 'btnViewReport')
    ACT.wait_element_clickable(driver, By.ID, 'btnViewReport')
    time.sleep(5)



def go_to_report_ip_Enterprise(driver):

    # Click "inpatient"
    inpatient = driver.find_element_by_id('aModuleSIP101')
    inpatient.click()

    # Click "report"
    report = driver.find_element_by_id('aIPModuleWorkplans')
    report.click()
    ACT.wait_presence_element_xpath(driver,'//span[text()="Inpatient Enterprise Reports"]')

    # Click "Inpatient Enterprise Reports"
    enterprice_link = driver.find_element_by_xpath('//span[text()="Inpatient Enterprise Reports"]')
    enterprice_link.click()
    # wait
    ACT.wait_invisibility_of_element_located(driver)



def go_to_report_ip_Standard(driver):
    # Click "inpatient"
    ACT.wait_element_clickable(driver, By.ID, 'aModuleSIP101')
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


def find_report_ip(driver, report_name):

    ACT.wait_presence_element(driver,'spnSearch')
    #ACT.wait_invisibility_of_element_located(driver)

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


def report_result_find_text(driver,report_name):
    driver.find_element_by_xpath('//br[text()="'+report_name+'"]')


def add_filters_besides_default_ones(driver):

    # set up filters
    add_icon = driver.find_element_by_id('btnInsertClause')
    add_icon.click()

    # add filters besides the default ones
    driver.find_element_by_id('customsearch-grid-div')
    fields = driver.find_elements_by_xpath(
        './/div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr')
    fields_len = fields.__len__()
    print('-----------fields_len = fields.__len__()-------------')
    field_last = driver.find_element_by_xpath(
        './/div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[3]')
    field_last.click()

    fields_lis = driver.find_elements_by_xpath('//div[@class="k-animation-container"][1]/div/ul/li')
    print(fields_lis.__len__())
    for li in fields_lis:
        print(li.text)

    # Case State - First Version DRG Type
    # value
    field_name = 'DRG Type'
    field_name = driver.find_element_by_xpath(
        '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + field_name + '"]')
    field_name.click()

    value_a = driver.find_element_by_xpath(
        './/div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[5]/div/div[4]/span/a')
    value_a.click()

    ACT.wait_invisibility_of_element_located(driver)
    ACT.wait_element_clickable(driver, By.XPATH, '//div[@id="dvLookupuGrid"]/div[@class="k-grid-content"]/table/tbody/tr[1]')
    value_select = driver.find_element_by_xpath(
        '//div[@id="dvLookupuGrid"]/div[@class="k-grid-content"]/table/tbody/tr[1]')
    value_select.click()
    print('-----------set_report_filters------------')

def report_group_by():
    print('----------------report_group_by-----------------------')

def view_report_by_default_filters(driver):

    btnViewReport = driver.find_element_by_id('btnViewReport')
    ACT.wait_element_clickable(driver, By.ID, 'btnViewReport')
    btnViewReport.click()
    ACT.wait_invisibility_of_element_located(driver)
    print('--------view_report_by_default_filters------------')

def swiitch_to_report_view_page(driver, report):
    window1 = driver.window_handles[1]
    driver.switch_to.window(window1)
    print('------window1------')
    ACT.wait_until_title_contains(driver, report)
    print(window1)
    print(driver.title)
    print('---wait_presence_element--------RW_ReportToolbar_ExportGr_FormatList_DropDownList----------')
    print('-----driver.execute_script(document.redyState)--------')
    print(driver.execute_script('return document.readyState'))
    ACT.wait_document_completed(driver)
    # if report == 'Case Listing':
    #     ACT.wait_presence_element(driver, 'RdlViewer_ctl01_ctl05_ctl00')
    # else:
    #     ACT.wait_presence_element(driver, 'RW_ReportToolbar_ExportGr_FormatList_DropDownList')

    # take a screnshot
    print('---------take a screnshot-------------')
    driver.save_screenshot('pictures/' + report + '.png')

    print('swiitch_to_report_view_page---------end')

def export_report(driver, report):
    print('-------------export_report------------------')
    # click "format"
    # case list RdlViewer_ctl01_ctl05_ctl00
    if report == 'Case Listing':
      format_list = driver.find_element_by_id('RdlViewer_ctl01_ctl05_ctl00')
    else:
      format_list = driver.find_element_by_id('RW_ReportToolbar_ExportGr_FormatList_DropDownList')
    format_list.click()
    # select a formt
    PDF = driver.find_element_by_xpath("//option[text()='Acrobat (PDF) file']")
    PDF.click()

    # formats_options = driver.find_element_by_xpath("//select[@id='RW_ReportToolbar_ExportGr_FormatList']/option[0]")
    # print(formats_options)

    ACT.wait_element_clickable(driver,By.LINK_TEXT,'Export')
    # take a screnshot
    driver.save_screenshot('pictures/'+report + '.png')
    # click "Export"
    expoert_btn = driver.find_element_by_link_text('Export')
    #expoert_btn = driver.find_element_by_id('RW_ReportToolbar_ExportGr_Export')
    expoert_btn.click()

    k = PyKeyboard()
    k.tap_key(k.enter_key)


