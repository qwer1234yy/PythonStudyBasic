import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    a= 10
    b=4

    def setUp(self):
        pass


    def test_test1(self):

        # self.assertNotIn(member='test',container='testTTTT')
        # assert 'test' not in 'test test'
        # self.assertEqual(self.a, self.b, 'a not equal b')
        AssertionError().with_traceback(tb=[T])
        print('afet')




    # @unittest.expectedFailure
    # def test_test2(self):
    #     print('test_test2')
    #
    # def test_test3(self):
    #     print('test_test3')
    #
    # def test_test4(self):
    #     print('test_test4')
    #
    def tearDown(self):

        print('tearDown')


if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(PythonOrgSearch('test_test1'))
    # result = unittest.TextTestRunner().run(suite)
    # print(result.expectedFailures)
