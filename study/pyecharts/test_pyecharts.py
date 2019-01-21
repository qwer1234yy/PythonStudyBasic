import unittest
from pyecharts import Bar


class MyTestCase(unittest.TestCase):
    def test_bar(self):
        bar = Bar("2019-01 A招聘网软件测试职位统计", "个数")
        bar.add("软件测试(各种软件测试)",
                ["上海", "深圳", "广州", "北京", "杭州", "武汉", '成都', '南京', '苏州', '西安', '长沙', '重庆'],
                [3251, 2712, 1996, 1455, 1312, 1039, 901, 890, 556, 438, 435, 367],
                is_more_utils=True, is_label_show=True)

        bar.render()

    def test_bar2(self):
        """
                1-5k    5-10k   10-15k  15-20k  20K以上
        上海:   212     233     232      223     123
        深圳：  212     233     232      223     123
        广州：  212     233     232      223     123

        """
        pass

    def test_bar3(self):
        """
                软件测试    功能测试   自动化测试  测试开发  性能测试
        上海:      212         233     232        223     123
        深圳：     212         233     232        223     123
        广州：     212         233     232        223     123

        """
        pass

    def test_bar4(self):
        pass


if __name__ == '__main__':
    unittest.main()
