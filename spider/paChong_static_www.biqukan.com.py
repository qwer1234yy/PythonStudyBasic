from bs4 import BeautifulSoup
import requests

url1 = 'https://www.biqukan.com/24_24164/8465767.html'
url2 = 'https://xueqiu.com/'
cookies_1 = {
    'UM_distinctid': '16740ec5ca3114-0c922aa24b036a-37664109-144000-16740ec5ca4f0',
    'fikker-rWK3-6KHs': 'T9T5b7lYVJReTQviPm2IdLPyHu83RwFM',
    'CNZZDATA1260938422': '767105970-1542980742-%7C1543034748'
}
headers = {
    "Accept": "*/*",
    'content-type': 'application/x-javascript',
    "If-None-Match": "1543028907",
    "Accept-Encoding": "gzip, deflate",
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'}
response = requests.get(url1, verify=False, cookies=cookies_1, headers=headers)

html1 = response.text
print(html1)
