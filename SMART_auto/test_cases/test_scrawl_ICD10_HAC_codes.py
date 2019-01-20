import unittest
import requests
from bs4 import BeautifulSoup


class MyTestCase(unittest.TestCase):

    def test_save_HAC_Codes_as_excel(self):
        pass

    def test_scrawl_ICD10HAC_codes(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Host': 'www.cms.gov'
        }
        # url = 'https://www.cms.gov/icd10manual/version31R-fullcode-cms/P0383.html'
        url = 'https://www.cms.gov/icd10manual/version31R-fullcode-cms/P1050.html'
        response = requests.get(url=url, headers=headers)
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
        HAC_ICD_codes = {}

        code_tables = bs.select('table.codelst')
        for t in range(0, code_tables.__len__()):
            # print('-----------code_types_descriptions----------------------------')
            # print(code_types_descriptions[t].text)
            HAC_ICD_codes['code_type_desc'] = code_types_descriptions[t].text

            # print('-----------code_types----------------------------')
            # print(code_types[t].text)
            HAC_ICD_codes['code_type'] = code_types[t].text

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
            HAC_ICD_codes['codes'] = codes

            for i in HAC_ICD_codes:
                print(HAC_ICD_codes[i])


if __name__ == '__main__':
    unittest.main()
