import unittest, os


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(os.getcwd())
        print(os._exists('ip_report_names.txt'))
        print(os.getcwd())


if __name__ == '__main__':
    unittest.main()
