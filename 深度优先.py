from bs4 import BeautifulSoup
import requests

class Stack:
    def __init__(self):
        self.st = []
    def pop(self):  #出栈函数
        return self.st.pop()#取列表的最后一个元素，并删除它
    def push(self,obj): #压栈函数
        self.st.append(obj)
    def empty(self):    #判断栈是否为空
        return len(self.st)==0

start_url = 'http://127.0.0.1:5000'
urls = []
stack = Stack()
stack.push(start_url)
while not stack.empty():
    url = stack.pop()
    if url == 'http://127.0.0.1:5000':
        url = 'http://127.0.0.1:5000/books.html'
    if url not in urls:
        urls.append(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        print(soup.find('h3').text)
        divs = soup.select('div')
        if len(divs)>0:
            print(divs[0].text)
        imgs = soup.select('img')
        if len(imgs)>0:
            imgurl = imgs[0]['src']
            data = requests.get(start_url+'/'+imgurl)
            fp = open('downloaded '+ imgurl, 'wb')
            fp.write(data.content)
            fp.close()

