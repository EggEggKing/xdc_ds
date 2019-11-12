import requests
from bs4 import BeautifulSoup
import re

def getInfo(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    texts = re.findall(r'<p>(.*?)</p>',r.text,re.S)
    for i in texts:
        f.write(i+'\n')

url = 'http://www.doupoxs.com/doupocangqiong/'
r = requests.get(url)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text,'lxml')
alist = soup.select('div.xsbox.clearfix > ul > li > a')
urls = []
for i in alist:
    urls.append('http://www.doupoxs.com'+i['href'])
f = open('doupo.txt','a',encoding='utf-8')
for i in urls[:5]:
    getInfo(i)

f.close()



