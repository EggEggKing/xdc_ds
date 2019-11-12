import requests
from bs4 import BeautifulSoup
import sqlite3

class weatherDB:
    def opendb(self):
        self.conn = sqlite3.connect("weather.db")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('create table weather(wcity varchar(16),wdate varchar(16),wweather varchar(64),wtemp varchar(32))')
        except:
            self.cursor.execute('delete from weather')

    def close(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def insert(self,city,date,weathe,temp):
        self.cursor.execute('insert into weather values(?,?,?,?)',(city,date,weathe,temp))
        print('inserted')

    def showData(self):
        self.cursor.execute('select * from weather')
        values = self.cursor.fetchall()
        print(values)

db = weatherDB()
db.opendb()
db.insert('深圳','十月九日','晴天','多云')
db.showData()
db.close()