# coding:utf-8

import unittest
from study.HTMLTestRunner_test import HTMLTestRunner
import os

current_path = os.getcwd()  # 当前文件路径
case_path = os.path.join(current_path, "case")  # 用例路径
# 存放报告路径
report_path = os.path.join(current_path, "report")

# discover找出以test开头的用例
def all_case():
    # discover = unittest.defaultTestLoader.discover(case_path, pattern="test*
    discover = unittest.defaultTestLoader.discover('testCases/', pattern="test*.py")
    return discover

if __name__ == "__main__":
    # 测试报告为result.html
    # result_path = os.path.join(report_path, "result.html")
    result_path = 'result/result.html'
    # 打开文件，把结果写进文件中，w，有内容的话，清空了再写进去
    fp = open(result_path, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="测试报告",
                                           description="用例执行情况")
    # 调用all_case函数返回值
    runner.run(all_case())

    # 有开有闭，关闭刚才打开的文件
    fp.close()