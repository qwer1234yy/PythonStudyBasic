import SMART.Smart_urls as base_url
import time
import SMART.Smart_common_settings as S_set
import SMART.Smart_com_acts as Act


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
    Act.wait_presence_element(driver,'aModuleSIP101')
    Act.wait_invisibility_of_element_located(driver)

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
        if not(line.strip().startswith('-')):
         fields.append(line.strip())
    fields_f.close()
    return fields

