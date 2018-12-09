import unittest, urllib3,json


class MyTestCase(unittest.TestCase):

    url_base = 'https://www.ximalaya.com'
    url_login = url_base + '/passport/v4/security/popupLogin'
    url_checkAccount = url_base + '/passport/login/checkAccount'
    http = urllib3.PoolManager()
    cookies = {
        'x_xmly_traffic': 'utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A',
        'device_id': 'xm_1544340538001_jpgkhdht1cyhsl',
        'Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070': '1544340539',
        'Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070': '1544340539'
    }
    login_headers = {
    'Accept': 'application/json,text/plain,*/*',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/68.0.3440.106 Safari/537.36',
    'Cookie': 'x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_'
              'term%253A%2526utm_from%253A;device_id=xm_1544340538001_jpgkhdht1cyhsl;Hm_lvt_4a7d8ec50cfd6af753c4f8a'
              'ee3425070=1544340539;Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1544340539',
    'Referer': 'https://www.ximalaya.com/',
    'Origin': 'https://www.ximalaya.com',
    'Content-Length': '232',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Connection': 'keep-alive',
    'Host': 'www.ximalaya.com'
    }
    fields_login = {
        'password': 'dmlHqvAECDYs0hMFWlC+qQWtGaXFy91od+ZkiID1ozvWIMuEjKPPi8lYZumCvKY3sbwhCQEwfYLYuJD2fxk+RFzlj7euX19mNfIPqBJdPfM4rGgV60/KKcjT7FTwYBsCKv3C7w8YMgYqNiO2hPtGxx3qzvS1lG4LXhcp7pn6o0U=',
        'rememberMe': 'false',
        'account': '15280928790'
    }
    fields_checkAccount = {
        'email': '15280928790'
    }

    def test_login(self):
        resp = self.http.request(method='post', url=self.url_login, headers=self.login_headers, fields=self.fields_login)
        # login_return_json = json.loads(resp.data.decode('utf-8'))
        # json.loads(r.data.decode('utf-8'))
        print(resp.status)
        login_return_json = resp.data
        print(login_return_json)

    def test_check_account(self):
        resp = self.http.request(method='post', url=self.url_checkAccount, headers=self.login_headers,
                                 fields=self.fields_checkAccount)
        # login_return_json = json.loads(resp.data.decode('utf-8'))
        # json.loads(r.data.decode('utf-8'))
        print(resp.status)
        login_return_json = resp.data
        print(login_return_json)

if __name__ == '__main__':
    unittest.main()
