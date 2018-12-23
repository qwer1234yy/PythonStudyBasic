import unittest
from unittest_study import ReportGenerator

class TestCaseInfo(object):
    """description of class"""

    def __init__(self, id="",name="",owner="",result="Failed",starttime="",endtime="",errorinfo=""):
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.errorinfo = errorinfo

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = TestCaseInfo(id='111', name='jion', owner='jdo',result='Failed', starttime='', endtime='',errorinfo='error')
        report_result= ReportGenerator.ReportGenerator()
        report_result.WriteHTML(result)
        report_result.CreateHtmlFile()

    def test_CreateTestResultFile(self):
        print('eeeeeeeeeeeeeeee')
        report_result = ReportGenerator.ReportGenerator()
        report_result.CreateHtmlFile()


if __name__ == '__main__':
    unittest.main()
