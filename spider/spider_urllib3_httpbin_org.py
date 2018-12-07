import unittest, urllib3,json


class MyTestCase(unittest.TestCase):

    url = "http://httpbin.org"
    url_spec_json = url + '/spec.json'
    url_robots_txt = url + '/robots.txt'
    http = urllib3.PoolManager()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    cookies = '_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_hour=1'
    Accept = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    headers = {
        'user_agent': user_agent,
        'Host': 'httpbin.org',
        'Cookie': cookies,
        'Accept': Accept,
        'Referer': 'http://httpbin.org/'
    }

    def test_something(self):
        response = self.http.request(method='get', url= self.url, fields=None, headers=self.headers)
        # 这个地方response 为何不提示
        print(response.read())
        print(response.status)
        print(response.headers)
        print(response.reason)
        print(response.data)
        print(response.msg)

    def test_get_spec(self):
        response = self.http.request(method='get', url=self.url_httpbin_org_spec_json, headers=self.headers)
        print(response.read())
        print(response.data)
        print(response.status)
        json_spec = json.loads(response.data.decode('utf-8'))
        print(json_spec['basePath'])
        print(json_spec['host'])
        print(json_spec['definitions'])
        print(json_spec['info'])
        print(json_spec['paths'])
        print(json_spec['protocol'])
        print(json_spec['tags'][0])
        specs = {}

        for i in range(0, 9):
         specs[json_spec['tags'][i]['description']] = json_spec['tags'][i]['name']

        for item in specs:
            print(specs[item].__str__() + ': ' + item.__str__())

    def test_get_icons(self):
        url = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMCAyMCI+ICAgIDxwYXRoIGQ9Ik0xMy40MTggNy44NTljLjI3MS0uMjY4LjcwOS0uMjY4Ljk3OCAwIC4yNy4yNjguMjcyLjcwMSAwIC45NjlsLTMuOTA4IDMuODNjLS4yNy4yNjgtLjcwNy4yNjgtLjk3OSAwbC0zLjkwOC0zLjgzYy0uMjctLjI2Ny0uMjctLjcwMSAwLS45NjkuMjcxLS4yNjguNzA5LS4yNjguOTc4IDBMMTAgMTFsMy40MTgtMy4xNDF6Ii8+PC9zdmc+'
        r = self.http.request(method='get', url=url)
        print(r)
        with open('icon.jpg', 'ab+') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
                f.flush()


if __name__ == '__main__':
    print('__name__ == __main__')
    unittest.main()
