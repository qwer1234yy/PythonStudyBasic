import unittest,requests,json,time
from bs4 import BeautifulSoup


class MyTestCase(unittest.TestCase):
    def test_something(self):
        url = 'http://image.baidu.com/'
        url2 = 'http://d.hiphotos.baidu.com/image/h%3D300/sign=57945c6810950a7b6a3548c43ad0625c/c8ea15ce36d3d539ad9c089d3787e950342ab0ce.jpg'
        url3 = 'http://b.hiphotos.baidu.com/image/h%3D400/sign=e55aa7ae80b1cb1321693d13ed5556da/0ff41bd5ad6eddc4802878ba34dbb6fd536633a0.jpg'
        url4 = "http://image.baidu.com/search/acjson?tn=resultjson_com&catename=pcindexhot&ipn=rj&ct=201326592&is=&fp=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=pcindexhot&face=0&istype=2&qc=&nc=1&fr=&pn=0&rn=30 HTTP/1.1"
        response = requests.get(url4)

        html = json.loads(response.text)

        imageURLs = html['data']
        for image in imageURLs:
            print(image['hoverURL'])
            responseHoverurl = requests.get(image['hoverURL'])
            print(responseHoverurl.iter_content())
            try:
                f = open('../pics/baidu_'+str((time.time()))+'.jpg', 'ab+')
                print("fffffffffffffffffffff")
                for chunk in responseHoverurl.iter_content(chunk_size=1024):
                    f.write(chunk)
                    f.flush()
            finally:
                if f:
                        f.close()


if __name__ == '__main__':
    unittest.main()
