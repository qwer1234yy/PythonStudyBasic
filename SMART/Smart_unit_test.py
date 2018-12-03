import unittest,time,os
import SMART.Smart_commons as SC
from selenium import webdriver
import SMART.Smart_com_acts as ACT
from docx import Document
from docx.shared import Inches
import SMART.KeyboardKeys as KEY



class MyTestCase(unittest.TestCase):
    def test_wait(self):
        driver = webdriver.Firefox()
        SC.login_(driver)

        # Click "inpatient"
        inpatient = driver.find_element_by_id('aModuleSIP101')
        inpatient.click()

        # Click "report"
        report = driver.find_element_by_id('aIPModuleWorkplans')
        report.click()

    def test_txt(self):
        fields_f = open('custom_search_fields.txt','r')
        lines = fields_f.readlines()
        fields = []
        print(lines.__len__())
        for line in lines:
             print(line.strip())
             fields.append(line.strip())
        fields_f.close()

    def test_get_default_fields(self):
        print('test_get_default_fields')

    def test_read_as_list(self):
        # custom_search_fields.txt
        items = SC.read_file_as_list('reports_names.txt')

        for item in items:
            print(item)
    def test_read_as_list_reports(self):
        # standard enterprise
        reports_dic_enterprise = SC.read_file_as_list_report_US299725('enterprise')
        reports_dic_standard = SC.read_file_as_list_report_US299725('standard')

        enterprise = list(reports_dic_enterprise.values())

        for i in enterprise:
            print(i)


    def test_python_docx(self):
        document = Document()

        document.add_heading('Document Title', 0)

        p = document.add_paragraph('A plain paragraph having some ')
        p.add_run('bold').bold = True
        p.add_run(' and some ')
        p.add_run('italic.').italic = True

        document.add_heading('Heading, level 1', level=1)
        document.add_paragraph('Intense quote', style='Intense Quote')

        document.add_paragraph(
            'first item in unordered list', style='List Bullet'
        )
        document.add_paragraph(
            'first item in ordered list', style='List Number'
        )

        document.add_picture('pictures/DRG Clinical Profile.png', width=Inches(1.25))

        records = (
            (3, '101', 'Spam'),
            (7, '422', 'Eggs'),
            (4, '631', 'Spam, spam, eggs, and spam')
        )

        table = document.add_table(rows=1, cols=3)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Qty'
        hdr_cells[1].text = 'Id'
        hdr_cells[2].text = 'Desc'
        for qty, id, desc in records:
            row_cells = table.add_row().cells
            row_cells[0].text = str(qty)
            row_cells[1].text = id
            row_cells[2].text = desc

        document.add_page_break()

        document.save('demo.docx')
    def test_docx_for_299725(self):

        pictures = 'pictures/DRG Clinical Profile.png'
        headings = 'Test Case 123456'
        SC.write_test_result_as_docx(pictures,headings)

    def test_kayBoeard(self):

        VK_CODE = {
            'enter': 0x0D,
            'ctrl': 0x11,
            'v': 0x56,
            'shift': 0x10}
        print(VK_CODE['enter'])
        KEY.KeyboardKeys.keyDown(17)

if __name__ == '__main__':
    unittest.main()
