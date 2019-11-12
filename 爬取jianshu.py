import requests
from bs4 import BeautifulSoup
import re
import csv

# f = open('jianshu.csv','w',encoding='utf-8',newline="")
# writer = csv.writer(f)
# writer.writerow(('title','text','writer'))

urls = ['https://www.jianshu.com/c/bDHhpk?order_by=added_at&page={}'.format(str(i)) for i in range(1,5)]
for url in urls:
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    r = requests.get(url,headers=headers)
    r.encoding = 'utf-8'
    # soup = BeautifulSoup(r.text,'lxml')
    # lis = re.findall(r'<li .*?">(.*?)</li>',r.text,re.S)
    # for i in lis:#没写完

    titles = re.findall(r'<a class="title" .*?">(.*?)</a>',r.text,re.S)
# titles = soup.select('div.content > a.title')
# title = []
# for i in titles:
#     title.append(i.text)
    text = re.findall(r'<p class="abstract">(.*?)</p>',r.text,re.S)
    writer = re.findall(r'<a class="nickname" .*?">(.*?)</a>',r.text,re.S)
    list = [titles, text, writer]
    print(list)
    # writer.writerow(list)
    print('------------------------')
# f.close()