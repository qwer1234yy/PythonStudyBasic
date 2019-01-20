import unittest
from spider.job51 import assists


class MyTestCase(unittest.TestCase):
    def test_format_salary(self):
        assists.format_salary('25-40万/年')
        assists.format_salary('2-2.5万/月')


if __name__ == '__main__':
    unittest.main()
