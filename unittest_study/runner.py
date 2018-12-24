import unittest
from unittest_study.test_cases import test1,test2
from HTMLTestRunner_test.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # 1
    # suite = unittest.TestSuite()
    # suite.addTest(test1.MyTestCase('test_a1'))
    # suite.addTest(test2.MyTestCase('test_a1'))
    # f= open('report.html','w',encoding='utf-8')
    # runer = HTMLTestRunner(stream = f, title ='report test',description = 'testt',verbosity = 2)
    # runer.run(suite)


    #2
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover('test_cases',pattern='test*.py')
    # for i in discover:
    #     print(i)
    #     suite.addTest(i)
    suite.addTests(discover)
    result = unittest.TextTestRunner().run(suite)

    print(result)
    print(type(result))

    #3
    # suite = unittest.TestSuite()
    # discover = unittest.defaultTestLoader.discover('test_cases', pattern='test*.py')
    # suite.addTests(discover)
    # f= open('report.html','w',encoding='utf-8')
    # runer = HTMLTestRunner(stream = f, title ='report test',description = 'testt',verbosity = 2)
    # runer.run(suite)