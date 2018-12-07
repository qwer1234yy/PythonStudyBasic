import SMART.Smart_urls as base_url
import SMART.Smart_com_acts as Act
from docx import Document
from docx.shared import Inches
import os
from selenium.webdriver.common.by import By
import SMART.Smart_common_settings as settings


def login_(driver):

    driver.get(base_url.base_url)

    login_ele = driver.find_element_by_id('txtLoginid')
    password_ele = driver.find_element_by_id('txtPassword')
    login_ele_btn = driver.find_element_by_id('btnloginText')

    login_ele.clear()
    login_ele.send_keys('admin')
    password_ele.clear()
    password_ele.send_keys('Admin')
    login_ele_btn.click()
    # wait for login completed
    Act.wait_invisibility_of_element_located(driver)
    Act.wait_presence_element(driver, 'aModuleSIP101')
    Act.wait_element_clickable(driver, By.ID, 'aModuleSIP101')

def read_custom_fields():
    fields = open('custom_search_fields.txt', 'r')
    lines = fields.readlines()
    print(lines.__len__())
    for line in lines:
            print('----------' + line.strip() + '-------')
    fields.close()

def read_file_as_list(file_name):
    print('read_as_list' + file_name)
    fields_f = open(file_name, 'r')
    lines = fields_f.readlines()
    fields = []

    print(lines.__len__())
    for line in lines:
        print(line.strip())
        if not (line.strip().startswith('-')):
            fields.append(line)
    fields_f.close()
    return fields
def go_to_MS_report(driver):
    print(go_to_MS_report)
    MS_access = driver.find_element_by_id('aSlideMenuSelModuleIP101')
    MS_access.click()

    MS_report_glossary_access = driver.find_element_by_id('aModuleReportGlossary')
    MS_report_glossary_access.click()



def read_file_as_list_report_US299725(enterprise_or_standard):
    file_name = 'reports_names.txt'
    print('read_as_list' + file_name)
    fields_f = open(file_name, 'r')
    lines = fields_f.readlines()
    fields = []
    fields_enterprise = []
    fields_enterprise_num = []
    fields_standard = []
    fields_standard_num = []

    fields_enterprise_dic = {}
    fields_standard_dic = {}

    print(lines.__len__())
    for line in lines:
        print(line.strip())
        if not(line.strip().startswith('-')):
            if '-IPST' in line:
                print('-----------IP standard report-------------')
                fields_enterprise_num.append(line.strip()[-6:])
                fields_standard.append(line.strip()[0:-12])
                fields_standard_dic[line.strip()[-6:]] = line.strip()[0:-12]

            elif '-IPEN' in line:
                print('-----------IP enterprise report-------------')
                fields_standard_num.append(line.strip()[-6:])
                fields_enterprise.append(line.strip()[0:-12])
                fields_enterprise_dic[line.strip()[-6:]] = line.strip()[0:-12]
            else:
                print('-----------MS report-------------')
    fields_f.close()
    if enterprise_or_standard == 'standard':
        return fields_standard_dic
    elif enterprise_or_standard == 'enterprise':
        return fields_enterprise_dic


def write_test_result_as_docx(picture, test_case):

    if os.path.exists(settings.test_result_file_name):
        document = Document(settings.test_result_file_name)
    else:
        document = Document()
    document.add_heading(test_case, level=1)
    document.add_picture(picture, width=Inches(6.43))
    document.save(settings.test_result_file_name)

def file_exists_delete(file_path):
    if os.path.exists(file_path):
        print('------------file_exists_delete-----------')
        os.remove(file_path)