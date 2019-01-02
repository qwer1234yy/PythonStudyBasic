import requests,cookies,random

headers = {}
url1 = 'https://piaofang.maoyan.com/dashboard'

cookies_src =['_lxsdk_cuid=167504ce4f2c8-03dc56e99c05c-37664109-144000-167504ce4f3c8; _lxsdk=167504ce4f2c8-03dc56e99c05c-37664109-144000-167504ce4f3c8; __mta=108887485.1543240475910.1543240506364.1543240508578.4; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=167504ce4f3-7eb-700-5d7%7C%7C7']
dest_cookie=cookies.Cookies[random.randint(0, len(cookies.Cookies)-1)]
print(dest_cookie)
headers = {
'user-agent':'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0'
           }
#response = requests.get(url1,cookies=cookies, headers=headers)

#print(response)