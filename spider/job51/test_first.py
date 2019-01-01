import unittest, requests, time, re
import tools.DBconnectionsTool as DBconnectionsTool
from bs4 import BeautifulSoup


class position(object):

    def __init__(self, position, company, location, salary, date, quality):
        self.position = position
        self.company = company
        self.location = location
        self.salary = salary
        self.date = date
        self.quality = quality


class MyTestCase(unittest.TestCase):
    positions = ['功能测试', '软件测试', '自动化测试 软件', '测试开发', 'AI测试']
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,测试工程师,2,1.html'
    headers = {
        'Referrer Policy': 'no-referrer-when-downgrade',
        'Host': 'search.51job.com',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }

    def get_total_pages(self, url):
        # parser = BeautifulSoup(self.connect(self.url), features="html.parser")
        # total = parser.select_one('#jump_page p:first-child')
        # str = 'sjdfakjd受到收到共12页jd受到收到'
        str = self.connect(url).__str__()
        # result = re.search('%s.*%s' % ('共', '页'), str)
        result = re.search('%s[1-9]\d*%s' % ('共', '页'), str)
        # result = re.match('%s[1-9]\d*%s' % ('共', '页'), str)

        print(result.group())
        print('-------------')
        total_pages = int(result.group().__str__()[1:-1])
        return total_pages

    def connect(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'gbk'
        # print(response.text)

        return response.text

    def get_position_description(self, url):

        # url = 'https://jobs.51job.com/shanghai/98946673.html?s=01&t=0'
        parser = BeautifulSoup(self.connect(url), features="html.parser")

        details = parser.select('div.job_msg > p')
        detail = ''
        for i in details:
            detail = detail + i.text

        return detail

    def parse_html(self, url):
        # url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,软件测试,2,94.html'
        parser = BeautifulSoup(self.connect(url), features="html.parser")
        span_tests = parser.select('div#resultList div.el')
        span_tests.pop(0)

        positions = []

        for i in span_tests:

            position_ = i.select_one('p span a').text.strip()
            company = i.select_one('span.t2 a').text
            location = i.select_one('span.t3').text
            salary = i.select_one('span.t4').text

            date_tem = i.select_one('span.t5').text

            # 区分一下19年和18年
            if '01-' in date_tem:
                date = '2019-' + date_tem
            else:
                date = '2018-' + date_tem

            detail_url = i.select_one('p span a')['href']
            time.sleep(0.2)
            detail_description = self.get_position_description(detail_url)

            position = {}

            if '测试' not in position_:
                pass
            else:
                position['position_'] = position_

            position['company'] = company
            position['location'] = location
            position['salary'] = salary
            position['date'] = date
            position['detail_description'] = detail_description

            query = """INSERT INTO 51job_position_v2(position,company,location,salary,date,description)VALUES
             ('{0}', '{1}', '{2}','{3}','{4}','{5}')""".format(
                position_, company, location, salary, date, detail_description)
            DBconnectionsTool.connection.insert(self, query=query)
            positions.append(position)

        for i in positions:
            print(i)

    def test_ord_field(self):
        position = '软件测试'
        page_index = '1'
        url_ = 'https://search.51job.com/list/000000,000000,0000,00,9,99,软件测试,2,1.html?ord_field=1'
        total_pages = self.get_total_pages(url=url_)

    def test_get_started(self):

        position = '软件测试'

        url_base_positin = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{0},2,1.html'.format(position)
        total_pages = self.get_total_pages(url_base_positin)

        for page_index in range(1, total_pages + 1):
            url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{0},2,{1}.html'.format(position, page_index)
            print(url)
            self.parse_html(url)


if __name__ == '__main__':
    unittest.main()
