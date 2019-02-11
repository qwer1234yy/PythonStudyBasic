import unittest, xlrd, xlwt, openpyxl, os, time
import requests
from bs4 import BeautifulSoup
import sys_tools


class MyTestCase(unittest.TestCase):

    def test_sys_tools(self):
        HACCodes_target = sys_tools.base_path + '/SMART_auto/test_cases/US287156/HAC ICD10 Codes from scrawler-gov.xlsx'
        print(sys_tools.base_path)
        print(os.path.exists(HACCodes_target))

    def save_HAC_Codes_as_excel(self, HAC_ICD_codes, page_index):
        HACCodes_target = sys_tools.base_path + '/SMART_auto/test_cases/US287156/ICD10 HAC Codes grabbed from the website.xlsx'
        wb = openpyxl.load_workbook(HACCodes_target)
        HACICD10Code_sheet = wb['HACCodeP'+ page_index.__str__()]
        # HAC_ICD_code5 = {
        #     'code_type_desc': 'code_type_desc5',
        #     'code_type': 'code_type5',
        #     'codes':
        #         {
        #             'Test001': 'testetst1',
        #         }
        # }
        # HAC_ICD_code1 = {
        #     'code_type_desc': 'code_type_desc1',
        #     'code_type': 'code_type1',
        #     'codes':
        #         {
        #             'Test001': 'testetst1',
        #             'Test002': 'sdfsfdfs2'
        #         }
        # }
        # HAC_ICD_code2 = {
        #     'code_type_desc': 'test2',
        #     'code_type': 'test2',
        #     'codes':
        #         {
        #             'Test001': 'testetst1',
        #             'Test002': 'sdfsfdfs2',
        #             'Test003': 'sdfsfdfs3'
        #         }
        # }
        # HAC_ICD_code3 = {
        #     'code_type_desc': 'test3',
        #     'code_type': 'test3',
        #     'codes':
        #         {
        #             'Test001': 'testetst1',
        #             'Test002': 'sdfsfdfs2',
        #             'Test003': 'testetst3',
        #             'Test004': 'sdfsfdfs4',
        #             'Test005': 'sdfsfdfs5'
        #         }
        # }
        # HAC_ICD_code4 = {
        #     'code_type_desc': 'test4',
        #     'code_type': 'test4',
        #     'codes':
        #         {
        #             'Test001': 'testetst1',
        #             'Test002': 'sdfsfdfs2',
        #             'Test003': 'testetst3',
        #             'Test004': 'sdfsfdfs4',
        #             'Test005': 'sdfsfdfs5',
        #             'Test006': 'sdfsfdfs6',
        #             'Test007': 'sdfsfdfs7'
        #         }
        # }
        # HAC_ICD_codes = []
        # HAC_ICD_codes.append(HAC_ICD_code1)
        # HAC_ICD_codes.append(HAC_ICD_code2)
        # HAC_ICD_codes.append(HAC_ICD_code3)
        # HAC_ICD_codes.append(HAC_ICD_code4)
        print(HAC_ICD_codes.__len__())
        rows_len = 0
        for code in HAC_ICD_codes:
            sub_codes = code['codes']
            index = 0
            for start_row in range(rows_len + 2, rows_len + sub_codes.__len__() + 2):
                # HACICD10Code_sheet.cell(row=rows_len + 2, column=1).value = code[
                #                                                                 'code_type'] + '  \n' + code[
                #                                                                 'code_type_desc']
                keys = list(sub_codes.keys())
                HACICD10Code_sheet.cell(row=start_row, column=2).value = keys[index]
                HACICD10Code_sheet.cell(row=start_row, column=3).value = sub_codes[keys[index]]
                index = index + 1
            rows_len = rows_len + sub_codes.__len__()
        wb.save(HACCodes_target)

    def save_HAC_Codes_as_excel_p1052(self, HAC_ICD_codes):
        HACCodes_target = sys_tools.base_path + '/SMART_auto/test_cases/US287156/HAC ICD10 Codes from scrawler-gov.xlsx'
        wb = openpyxl.load_workbook(HACCodes_target)
        HACICD10Code_sheet = wb['HACICD10Code']
        print(HAC_ICD_codes.__len__())
        rows_len = 0
        for code in HAC_ICD_codes:
            sub_codes = code['codes']
            index = 0
            for start_row in range(rows_len + 2, rows_len + sub_codes.__len__() + 2):
                # HACICD10Code_sheet.cell(row=rows_len + 2, column=1).value = code[
                #                                                                 'code_type'] + '  \n' + code[
                #                                                                 'code_type_desc']
                keys = list(sub_codes.keys())
                HACICD10Code_sheet.cell(row=start_row, column=2).value = keys[index]
                HACICD10Code_sheet.cell(row=start_row, column=3).value = sub_codes[keys[index]]
                index = index + 1
            rows_len = rows_len + sub_codes.__len__()
        wb.save(HACCodes_target)

    def test_scrawl_ICD10HAC_codes_p1052(self):
        HAC_ICD_codes = []
        hac_url = 'https://www.cms.gov/icd10manual/version31R-fullcode-cms/P1052.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Host': 'www.cms.gov'
        }
        response = requests.get(url=hac_url, headers=headers)
        response.encoding = 'gbk'
        bs = BeautifulSoup(response.text, features="html.parser")
        code_tables = bs.select('table.codelst')
        code_types_descriptions = bs.select('p.titone')
        code_types_descriptions.insert(2, 'AND')
        code_types = bs.select('p.tittwo')
        code_types.insert(2, 'SECONDARY DIAGNOSIS')
        # P1052
        for t in range(0, code_tables.__len__()):
            HAC_ICD_code = {}
            if t == 2:
                HAC_ICD_code['code_type_desc'] = code_types_descriptions[t]
                HAC_ICD_code['code_type'] = code_types[t]
            else:
                HAC_ICD_code['code_type_desc'] = code_types_descriptions[t].text
                HAC_ICD_code['code_type'] = code_types[t].text

            trs = code_tables[t].select('tr')
            codes = {}
            for tr in trs:
                tds = tr.select('td')
                codes[tds[0].text] = tds[1].text
            HAC_ICD_code['codes'] = codes
            HAC_ICD_codes.append(HAC_ICD_code)
        self.save_HAC_Codes_as_excel(HAC_ICD_codes)

    def test_scrawl_ICD10HAC_codes(self):

        # for i in range(1083, 1096):
        for i in [1094,1091]:
            try:
                page_index = i.__str__()
                if i == 1095:
                    page_index = '0383'
                else:
                    pass

                hac_url = 'https://www.cms.gov/ICD10Manual/version36-fullcode-cms/fullcode_cms/P{0}.html'.format(
                    page_index)
                HAC_ICD_codes = []
                # hac_url = 'https://www.cms.gov/ICD10Manual/version36-fullcode-cms/fullcode_cms/P0383.html'

                # hac_url = 'https://www.cms.gov/icd10manual/version31R-fullcode-cms/P1049.html'

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                    'Host': 'www.cms.gov'
                }

                print(hac_url)
                response = requests.get(url=hac_url, headers=headers)
                time.sleep(3)
                response.encoding = 'gbk'
                bs = BeautifulSoup(response.text, features="html.parser")
                code_tables = bs.select('table.codelst')
                print('code_tables.__len__()')
                print(code_tables.__len__())
                code_types_descriptions = bs.select('p.titone')
                code_types = bs.select('p.tittwo')

                for t in range(0, code_tables.__len__()):
                    HAC_ICD_code = {}
                    # HAC_ICD_code['code_type_desc'] = code_types_descriptions[t].text
                    # HAC_ICD_code['code_type'] = code_types[t].text
                    trs = code_tables[t].select('tr')
                    codes = {}
                    for tr in trs:
                        tds = tr.select('td')
                        codes[tds[0].text] = tds[1].text
                    HAC_ICD_code['codes'] = codes
                    HAC_ICD_codes.append(HAC_ICD_code)
                self.save_HAC_Codes_as_excel(HAC_ICD_codes, page_index)
            except Exception as e:
                print(e)
                continue





if __name__ == '__main__':
    unittest.main()
