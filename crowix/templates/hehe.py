#coding=utf-8
import urllib
import re
import MySQLdb
from _mysql import MySQLError, NULL
from twisted.web.client import getPage
from hehe import save2MySQL

class spider:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.enable = 1
        
    def getPage(self,pageIndex):
        url = "http://www.dota2shop.cn/?h=矮人直升机&page=" + str(pageIndex)          
        page = urllib.urlopen(url)
        html = page.read()
        return html
    
    def getPageItems(self,html):
        myItems = re.findall('<div.*?class="price".*?<span>(.*?)</span>.*?class="name">(.*?)</div>',html,re.S)   
        if len(myItems):
            return myItems
        else:
            self.enable = 0
            return NULL
    
    def save2MySQL(self,prices):
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='dota2',port=3306)
            conn.set_character_set('utf8')
            cur=conn.cursor()
            cur.execute('create table if not exists  airenzhishengji(id int not null auto_increment, name varchar(40), price float, primary key (id))')
            for price in prices:
                value = [price[1].decode('utf-8'),price[0]]
                cur.execute('insert into airenzhishengji (name,price) values(%s,%s)',value)
            conn.commit()
            cur.close()
            conn.close()
            print ("write successed! page %s is down", self.pageIndex)
        except MySQLError as error:
            print ("MySQL %s", error)
            
    def start(self):
        print ("正在读取网站数据，请稍候...")
        while self.enable == 1:
            html = self.getPage(self.pageIndex)
            prices = self.getPageItems(html)
            if self.enable == 0:
                break
            self.save2MySQL(prices)
            self.pageIndex = self.pageIndex + 1
        print("DOWN!")
        
        
sp = spider()
sp.start()
    
      
        