import unittest
import HtmlTestRunner


class MyTestCase(unittest.TestCase):
    def test_1(self):
        print('test_1')
    def test_2(self):
        print('test_2')
    def test_3(self):
        print('test_3')
    def test_4(self):
        print('test_4')
    def test_5(self):
        print('test_5')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\yyang212\\PycharmProjects\\PythonStudy\\study\\HTMLTestRunner_test\\result'))
