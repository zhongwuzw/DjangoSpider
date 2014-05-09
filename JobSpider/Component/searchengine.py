# -*- coding: utf-8 -*-
import requests
import urlparse
from JobSpider.models import UrlList,Link,LinkWords,WordList,WordLocation
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        pass
    
    def __del__(self):
        pass

    #为每个网页建立索引
    def addToIndex(self,url,soup):
        if self.isIndexed(url):
            return
        print u'索引   %s' %url
        text = self.getTextOnly(soup)
        words = self.separateWords(text)
        url_id,created = UrlList.objects.get_or_create(url = url) 
        for i in range(len(words)):
            word = words[i]
            word_id,created = WordList.objects.get_or_create(word = word)
            word_location = WordLocation()
            word_location.word_id = word_id
            word_location.url_id = url_id
            word_location.location = i
            word_location.save()
            
    #从一个HTML中提取文字（不带标签的）
    def getTextOnly(self,soup):
        v = soup.string
        if v == None:
            result_text = u''
            for i in soup.contents:
                sub_text = self.getTextOnly(i)
                result_text += sub_text + '\n'
            return result_text
        else:
            return v.strip()
    #根据任何非空白字符进行分词处理
    def separateWords(self,text):
        li = [text[i] for i in range(len(text)) if text[i] >= u'\u4e00' and text[i] <= u'\u9fff']
        return li
    #如果url已经建立索引，则返回true
    def isIndexed(self,url):
        try:
            p = UrlList.objects.get(url = url)
        except UrlList.DoesNotExist:
            return False
        else:
            return True
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
            pages = new_pages
            

class Searcher:
    def __init__(self):
        pass
    #获取查询串的查询结果
    def getMatchRows(self,q):
        text = q
        final_li = []
        li = [text[i] for i in range(len(text)) if text[i] >= u'\u4e00' and text[i] <= u'\u9fff']
        for q_part in li:
            s = set([])
            p = WordList.objects.get(word = q_part)
            for i in p.wordlocation_set.all():
                s.add(i.url_id.url)
            final_li.append(s)
        final_set = final_li[0]
        for x in range(len(final_li) - 1):
            final_set = final_set.intersection(final_li[x+1])
        print final_set

