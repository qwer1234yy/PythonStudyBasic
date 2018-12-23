import unittest
from lxml import etree


class MyTestCase(unittest.TestCase):
    def test_something(self):
        text = '''
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">第一个</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-0"><a href="link5.html">a属性</a>
             </ul>
         </div>
        '''
        html = etree.HTML(text)  # 初始化生成一个XPath解析对象
        result = etree.tostring(html, encoding='utf-8')  # 解析对象输出代码
        print(type(html))
        print(type(result))
        print(result.decode('utf-8'))

    def test_readHtml(self):
        html = etree.parse('../unittest_study/TestResult2.html', etree.HTMLParser())  # 指定解析器HTMLParser会根据文件修复HTML文件中缺失的如声明信息
        result = etree.tostring(html)  # 解析成字节
        # result=etree.tostringlist(html) #解析成列表
        print(type(html))
        print(type(result))
        print(result)
    def test_get_all_elements(self):
        html = etree.parse('../unittest_study/TestResult2.html', etree.HTMLParser())
        result = html.xpath('//*')  # //代表获取子孙节点，*代表获取所有

        print(type(html))
        print(type(result))
        print(result)


if __name__ == '__main__':
    unittest.main()
