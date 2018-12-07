import unittest, json
import urllib3


class MyTestCase(unittest.TestCase):

    url = "http://www.ctrip.com"
    url_httpbin_org = 'http://httpbin.org'
    partial_url_robots_txt = '/robots.txt'
    http = urllib3.PoolManager()

    def test_urlopen_get(self):
        r = self.http.request('GET', self.url + "/get")
        print(r.data.decode())
        print(r.status)

    def test_getWithParams(self):
        # 带参数的get

        r = self.request('get', 'http://www.baidu.com/s', fields={'wd': '周杰伦'})
        # print(r.data.decode())
        # 我们可以通过dir()查看任何对象的所有的属性和方法
        print(dir(r))

    def test_postWithParams(self):
        fields = {
            'name': 'xfy'
        }
        r = self.http.request('post', self.url + "/post", fields=fields)
        print(r.data.decode())

    def test_JSON_content(self):
        r = self.http.request('GET', 'http://httpbin.org/ip')
        json_load_result = json.loads(r.data.decode('utf-8'))
        print(json_load_result)

    def test_Binary_content(self):
        r = self.http.request('GET', 'http://httpbin.org/bytes/8')
        print(r.status)
        print(r.data)
        print(r.headers)
        print(r.read())
        print(r.reason)
        print(r.msg)
        print(r.version)



if __name__ == '__main__':
    unittest.main()
