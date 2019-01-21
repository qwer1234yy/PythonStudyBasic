import unittest, xlrd, xlwt, openpyxl, os, time
import requests
from bs4 import BeautifulSoup
import sys_tools


class MyTestCase(unittest.TestCase):

    def test_sys_tools(self):
        HACCodes_target = sys_tools.base_path + '/SMART_auto/test_cases/US287156/HAC ICD10 Codes from scrawler-gov.xlsx'
        print(sys_tools.base_path)
        print(os.path.exists(HACCodes_target))

    def save_HAC_Codes_as_excel(self, HAC_ICD_codes):
        HACCodes_target = sys_tools.base_path + '/SMART_auto/test_cases/US287156/HAC ICD10 Codes from scrawler-gov.xlsx'
        wb = openpyxl.load_workbook(HACCodes_target)
        HACICD10Code_sheet = wb['HACICD10Code']
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
                HACICD10Code_sheet.cell(row=rows_len + 2, column=1).value = code[
                                                                                'code_type'] + '  \n' + code[
                                                                                'code_type_desc']
                keys = list(sub_codes.keys())
                HACICD10Code_sheet.cell(row=start_row, column=2).value = keys[index]
                HACICD10Code_sheet.cell(row=start_row, column=3).value = sub_codes[keys[index]]
                index = index + 1
            rows_len = rows_len + sub_codes.__len__()
        wb.save(HACCodes_target)

    def test_scrawl_ICD10HAC_codes(self):

        HAC_ICD_codes = []
        for i in range(1041, 1054):
            hac_url = 'https://www.cms.gov/icd10manual/version31R-fullcode-cms/P{0}.html'.format(i.__str__())
            if i == 1053:
                hac_url = 'https://www.cms.gov/icd10manual/version31R-fullcode-cms/P0383.html'
            if i == 1049 or i == 1052:
                continue
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                'Host': 'www.cms.gov'
            }
            # hac_url = 'https://www.cms.gov/icd10manual/version31R-fullcode-cms/P1049.html'
            print(hac_url)
            response = requests.get(url=hac_url, headers=headers)
            response.encoding = 'gbk'
            bs = BeautifulSoup(response.text, features="html.parser")

            # '-----------code_types_descriptions----------------------------'
            code_types_descriptions = bs.select('p.titone')
            # '-----------code_types----------------------------'
            code_types = bs.select('p.tittwo')
            # HAC_ICD_codes = {
            #     'code_type_desc': '',
            #     'code_type': '',
            #     'codes':
            #         {
            #             'code': '',
            #             'code_desc': ''
            #         }
            # }
            code_tables = bs.select('table.codelst')
            print(code_tables.__len__())
            for t in range(0, code_tables.__len__()):
                HAC_ICD_code = {}
                # print('-----------code_types_descriptions----------------------------')
                # print(code_types_descriptions[t].text)
                HAC_ICD_code['code_type_desc'] = code_types_descriptions[t].text

                # print('-----------code_types----------------------------')
                # print(code_types[t].text)
                HAC_ICD_code['code_type'] = code_types[t].text

                # size = code_tables[t].select('tr').__len__()
                # print(size)

                trs = code_tables[t].select('tr')
                # print('-----------td values----------------------------')
                codes = {}
                for tr in trs:
                    tds = tr.select('td')
                    # print(tds[0].text)
                    # print(tds[1].text)
                    codes[tds[0].text] = tds[1].text
                HAC_ICD_code['codes'] = codes

                # for i in HAC_ICD_code:
                #     print(HAC_ICD_code[i])
                HAC_ICD_codes.append(HAC_ICD_code)

        self.save_HAC_Codes_as_excel(HAC_ICD_codes)

if __name__ == '__main__':
    unittest.main()
