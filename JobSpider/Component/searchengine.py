# -*- coding: utf-8 -*-
import requests
import urlparse

from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def dbCommit(self):
        pass
    #获取条目的id，并且如果条目不存在，就将其加入数据库
    def getEntryID(self,table,field,value,create_new = True):
        return None
    #为每个网页建立索引
    def addToIndex(self,url,soup):
        print u'索引   %s' %url
    #从一个HTML中提取文字（不带标签的）
    def getTextOnly(self,soup):
        return None
    #根据任何非空白字符进行分词处理
    def separateWords(self,text):
        return None
    #如果url已经建立索引，则返回true
    def isIndexed(self,url):
        return False
    #添加一个关联两个网页的链接
    def addLinkRef(self,url_form,url_to,link_text):
        pass
    #从一小组网页开始进行广度优先搜索，直至某一给定深度，期间为网页建立索引
    def crawl(self,pages,depth = 2):
        for i in range(depth):
            new_pages = set()
            for page in pages:
                r = requests.get(page)
                if r.status_code == requests.codes.ok:
                    soup = BeautifulSoup(r.text)
                    self.addToIndex(page, soup)
                    
                    links = soup.find_all('a')
                    for link in links:
                        if link.get('href') != None:
                            url = urlparse.urljoin(page,link['href'])
                            url = url.split('#')[0]
                            if url.startswith('http') and not self.isIndexed(url):
                                new_pages.add(url)
                            link_text = self.getTextOnly(link)
                            self.addLinkRef(page, url, link_text)
                    self.dbCommit()
            pages = new_pages