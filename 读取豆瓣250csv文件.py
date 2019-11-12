import requests
from bs4 import BeautifulSoup
import re
import csv

f = open('douban250.csv','w',encoding='utf-8',newline="")
writer = csv.writer(f)
writer.writerow(('title','author','publisher','date','price','rate','comment'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,50,25)]

url = 'https://book.douban.com/top250?start=0'
r = requests.get(url)
r.encoding = r.apparent_encoding
r = r.text
infos = re.findall(r'<tr class="item">(.*?)</tr>',r,re.S)
for i in infos:
    title = re.findall(r'title="(.*?)"',i,re.S)[0]
    print(title)
    sss = re.findall(r'<p class="pl">(.*?)</p>',i,re.S)[0]
    sss = str(sss).split('/')
    price = sss[-1]
    date = sss[-2]
    publisher = sss[-3]
    parts = len(sss)
    end = parts-3
    author = sss[0:end]
    if len(author)>0:
        author = "/".join(author)
    rate = re.findall('<span class="rating_nums">(.*?)</span>',i,re.S)[0]
    comment = re.findall('<span class="inq">(.*?)</span>',i,re.S)[0]
    list = [title,author,publisher,date,price,rate,comment]
    print(list)
    writer.writerow(list)
    print('------------------------')
f.close()