# -*- coding: utf-8 -*-
import redis
from django.test import TestCase
from JobSpider.Component.searchengine import Crawler,Searcher
# page_list = ['http://www.265.com']
# crawler = Crawler()
# crawler.crawl(page_list)
# searcher = Searcher()
# searcher.getMatchRows(u'家的钟')
r = redis.StrictRedis()
# r.set('foo','bar')
print r.get('foo')
r.hmset('dict',{'name':'Bob','id':'123'})
people = r.hgetall('dict')
print people


