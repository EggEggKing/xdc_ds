import requests
from bs4 import BeautifulSoup
import pymysql

class Stack:
    def __init__(self):
        self.st = []
    def pop(self):  #出栈函数
        return self.st.pop()#取列表的最后一个元素，并删除它
    def push(self,obj): #压栈函数
        self.st.append(obj)
    def empty(self):    #判断栈是否为空
        return len(self.st)==0

# conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='szhome')
# cursor = conn.cursor()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
start_url = 'http://bbs.szhome.com/User/comment-2644470.html'
urls = []
stack = Stack()
lay = 1#层数
stack.push((start_url,lay))
while not stack.empty():
    xx = stack.pop()
    url = xx[0]
    lay = xx[1]
    if (url not in urls) and (lay<=2):
        urls.append(url)
        r = requests.get(url,headers = headers)
        soup = BeautifulSoup(r.text,'lxml')
        titles = soup.select('a.title')
        for title in titles:
            print(title.text)
            # cursor.execute('insert into bbs values(%s)',title.text)

        names = soup.select('div.bg_withe.mb20.pdb20.fix')
        if(len(names))>0:
            lay = lay+1
            names = names[0].select('a.name')
            for name in names[::-1]:
                print(name.text)
                print('http://bbs.szhome.com'+name['href'])
                stack.push(('http://bbs.szhome.com'+name['href'],lay))
        print('--------------------------------------------------------------')
# cursor.close()
# conn.commit()
# conn.close()