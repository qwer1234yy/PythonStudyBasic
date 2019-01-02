import unittest
import urllib3

class MyTestCase(unittest.TestCase):
    def test_something(self):
        url = 'http://www.server.com/login'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {'username': 'cqc', 'password': 'XXXX'}
        headers = {'User-Agent': user_agent}

        # urllib.r
        # request = urllib2.Request(url, data, headers)
        # response = urllib2.urlopen(request)
        # page = response.read()
        # self.assertEqual(True, False)
        # url = 'http://www.baidu.com'
        # resp = request.urlopen(url)
        # # getcode() geturl()
        # print(resp.getheaders())
        # .出来的图标都代表什么事情
        #  proxy
        url = 'https://www.baidu.com'
        http = urllib3.PoolManager()
        headers = {'X-Something': 'value'}
        fields = {'arg': 'value'}
        resp = http.request('GET', 'http://httpbin.org/headers', headers=headers, fields=fields)
        print(resp.status)
        print(resp)
        # resp = http.request('POST', 'http://httpbin.org/get', fields=fields)

        http_proxy = urllib3.PoolManager('http://50.233.137.33:80', headers={'connection': 'keep-alive'})
        response = http_proxy.request('get',url)
        print(resp.status)
        print(response)

if __name__ == '__main__':
    unittest.main()
