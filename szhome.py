import requests
from bs4 import BeautifulSoup
import json
import re

headers = {'Content-Type': 'application/json','X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
url = 'http://bbs.szhome.com/user/comment-2644470.html'
userid = re.findall("(\d+)",url)[0]
print(userid)
url = 'http://bbs.szhome.com/UserControls/GetUserInfo'
data = {"id":userid}
data = json.dumps(data)

r = requests.post(url,data=data,headers=headers)
userinfo = json.loads(r.text)
print(userinfo["Data"][0]["UserName"])


