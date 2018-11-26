import unittest
import urllib3


class MyTestCase(unittest.TestCase):
    def test_urlopen(self):
        url = "http://www.ctrip.com"
        http = urllib3.PoolManager();
        r = http.request('GET', url + "/get")
        print(r.data.decode())
        print(r.status)
    def test_getWithParams(self):
        # 带参数的get
        http = urllib3.PoolManager();
        r = http.request('get', 'http://www.baidu.com/s', fields={'wd': '周杰伦'})
        # print(r.data.decode())
        # 我们可以通过dir()查看任何对象的所有的属性和方法
        print(dir(r))

    def test_postWithParams(self):
        url = "http://httpbin.org"
        fields = {
            'name': 'xfy'
        }
        http = urllib3.PoolManager()
        r = http.request('post', url + "/post", fields=fields)
        print(r.data.decode())
if __name__ == '__main__':
    unittest.main()
