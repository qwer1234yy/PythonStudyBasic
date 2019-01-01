import unittest
from spider.job51 import assists


class MyTestCase(unittest.TestCase):
    location = ['北京', '广州', '深圳', '重庆', '成都', '武汉', '杭州', '南京']
    query_all = "SELECT * from 51job_position_v1 where locate(substr,str)"
    query_salary_contain_year = "SELECT * from 51job_position_v1 where locate('年',salary)"

    def test_something(self):
        self.assertEqual(True, False)

    def test_get_count_location(self):
        print(assists.get_count_location(self, '成都'))


if __name__ == '__main__':
    unittest.main()
