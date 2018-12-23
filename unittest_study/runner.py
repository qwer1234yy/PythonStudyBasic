import unittest
from unittest_study.test_cases import test1,test2
from HTMLTestRunner_test.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test1.MyTestCase('test_a1'))
    suite.addTest(test2.MyTestCase('test_a1'))
    f= open('report.html','w',encoding='utf-8')
    runer = HTMLTestRunner(stream = f, title ='report test',description = 'testt',verbosity = 2)
    runer.run(suite)