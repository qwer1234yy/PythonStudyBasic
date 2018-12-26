import SMART.Smart_urls as base_url
import SMART.Smart_com_acts as Act
from docx import Document
from docx.shared import Inches
import os, time
from selenium.webdriver.common.by import By
import SMART.Smart_common_settings as settings
from SMART.Smart_tools import tools
import os


def read_report_names(enterprise_or_standard):

    file_name = r'C:\Users\yyang212\PycharmProjects\PythonStudy\SMART\Smart_regression\resources\ip_report_names.txt'
    print('read_report_names:' + file_name)
    report_file = open(file_name, 'r')
    lines = report_file.readlines()

    names_enterprise = []
    names_standard = []

    print('strat to read file:' + file_name)
    for line in lines:
        print(line.strip())
        if not(line.strip().startswith('-')):
            if '-standard' in line:
                print('-----------Find IP standard report-------------')
                names_standard.append(line.strip()[0:-9])

            elif '-enterprise' in line:
                print('-----------FInd IP enterprise report-------------')
                names_enterprise.append(line.strip()[0:-11])
            else:
                print('nor standard or enterprise')
                pass

    report_file.close()

    if enterprise_or_standard == 'standard':
        return names_standard
    elif enterprise_or_standard == 'enterprise':
        return names_enterprise


def take_screenshot(driver, report_name):
    if report_name == 'Top 50 CC/MCC Diagnoses':
        picture_path = '../screenshots/Top 50 CC_MCC Diagnoses.png'
    else:
        picture_path = '../screenshots/' + report_name + '.png'

    # if pic exists, delete it
    tools.file_exist_delete(picture_path)
    driver.save_screenshot(picture_path)