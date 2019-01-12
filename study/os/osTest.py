import unittest,os
from study.excel import excel_handler


class MyTestCase(unittest.TestCase):
    def test_something(self):
        excel_handler.MyTestCase.test_os(self)
        f_name = 'test.PNG'
        path = os.getcwd()
        print(path)



if __name__ == '__main__':
    unittest.main()
