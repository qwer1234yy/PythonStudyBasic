from bs4 import BeautifulSoup
import requests

url = 'http://api.xfsub.com/index.php?url=http://www.iqiyi.com/v_19rr7qhfg0.html#vfrm=19-9-0-1'
resp = requests.get(url)
print(resp.text)