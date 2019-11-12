import requests
from bs4 import BeautifulSoup
import pymysql

class MyDB:
    def opendb(self):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='mydb',charset='utf8')
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('create table weather(city varchar(20),date varchar(30),weather varchar(40),temp varchar(40))')
        except:
            self.cursor.execute('delete from weather')

    def insert(self,city,date,weather,temp):
        self.cursor.execute('insert into weather values(%s,%s,%s,%s)',(city,date,weather,temp))

    def showdata(self):
        self.cursor.execute('select * from weather')
        value = self.cursor.fetchall()
        print(value)

    def closedb(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

class Weather:
    def __init__(self):
        self.url = 'http://www.weather.com.cn/weather/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        self.cities = {'北京': '101010100', '上海': '101020100', '广州': '101280101', '深圳': '101280601'}
    def process(self,cities):
        db = MyDB()
        db.opendb()
        for i in cities:
            if i not in self.cities.keys():
                print(i+'can not be fond')
                return
            url = self.url+self.cities[i]+'.shtml'
            r = requests.get(url, headers=self.headers)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, "lxml")
            lis = soup.select("ul.t.clearfix > li")
            for li in lis:
                date = li.select('h1')[0].text
                weather = li.select('p[class="wea"]')[0].text
                temp = li.select('p[class="tem"]')[0].text.strip()
                db.insert(i,date,weather,temp)
                print(date, weather, temp)
        db.showdata()
        db.closedb()

wf = Weather()
wf.process(['北京','上海'])