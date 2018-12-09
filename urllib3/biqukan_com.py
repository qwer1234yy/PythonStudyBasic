import unittest, urllib3,requests


class MyTestCase(unittest.TestCase):

    url_base = 'https://www.biqukan.com/'
    # 重生之娱乐天王
    url_reborn_king = url_base + '/56_56280/'
    http = urllib3.PoolManager()
    headers_index = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'h-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/68.0.3440.106 Safari/537.36',
        'Cookie': 'fikker-kpOR-yMMP=UtideP169pQFUNAFmMyBI8NXMD9dg0Sd,'
                  'fikker-kpOR-yMMP=UtideP169pQFUNAFmMyBI8NXMD9dg0Sd,'
                  'UM_distinctid=16792212c1065a-02c5a1021107a8-37664109-144000-16792212c12245,'
                  'CNZZDATA1260938422=1013510005-1544340518-%7C1544340518',
        'Host': 'www.biqukan.com',
        'Connection': 'keep - alive'
    }
    headers_reborn_king = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'h-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/68.0.3440.106 Safari/537.36',
        'Cookie': 'fikker-kpOR-yMMP=UtideP169pQFUNAFmMyBI8NXMD9dg0Sd;'
                  'fikker-kpOR-yMMP=UtideP169pQFUNAFmMyBI8NXMD9dg0Sd;'
                  'UM_distinctid=16792212c1065a-02c5a1021107a8-37664109-144000-16792212c12245;'
                  'CNZZDATA1260938422=1013510005-1544340518-%7C1544340518',
        'Referer': 'https://www.biqukan.com/',
        'Connection': 'keep-alive',
        'Host': 'www.biqukan.com'
    }


    def test_index_page(self):
        resp = self.http.request(method='get',url=self.url_base,headers=self.headers_index)
        print(resp.data)
    def test_get_reborn_king(self):
        resp = self.http.request(method='get', url=self.url_reborn_king, headers=self.headers_reborn_king)
        print(resp.read())
        print(resp.data)

    def test_get_reborn_king_requests(self):
        resp = requests.get(method='get', url=self.url_reborn_king, headers=self.headers_reborn_king)
        print(resp.text)

if __name__ == '__main__':
    unittest.main()
