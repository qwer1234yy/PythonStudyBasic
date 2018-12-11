import unittest, urllib3


class MyTestCase(unittest.TestCase):

    url_response_code = 'https://www.restapitutorial.com/httpstatuscodes.html'
    http = urllib3.PoolManager()
    'cookie: __utmc=15483189; __utmz=15483189.1544413616.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utma=15483189.93414993.1544413616.1544413616.1544413616.1; __utmb=15483189.1.10.1544413616'

    headers_response_code = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    def test_get_response_code(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        resp = self.http.request(method='get', url=self.url_response_code, headers=self.headers_response_code)
        print(resp.data)


if __name__ == '__main__':
    unittest.main()
