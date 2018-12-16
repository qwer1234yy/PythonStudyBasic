import unittest


class MyTestCase(unittest.TestCase):
    def test_str_join_by_seperator(self):
        str_list = ['sdfasdf','dfa','sdaf','afsdf',]
        str_join = ''
        seperator = ','
        for i in str_list:
           str_join =  seperator.join(str_list)
        print(str_join)
    def test_iter_dic(self):
        blog = {'1': '中国石油大学', '2': '浙江大学', '3': '南京航空航天大学'}
        for key, value in blog.items():
            print('{0}:{1}'.format(key,value))
        for key in blog.items():
            print(key)
        for key in blog.keys():
            print(key)
        for key in blog.values():
            print(key)
    def test_str_encoding(self):
        # 文件存储的无非是文本和二进制这两种格式
        print('jon原因'.encode())
        print(b'jon\xe5\x8e\x9f\xe5\x9b\xa0'.decode())


if __name__ == '__main__':
    unittest.main()
