# -*- coding: utf-8 -*-
from django.test import TestCase
from JobSpider.Component.searchengine import Crawler,Searcher
# page_list = ['http://www.265.com']
# crawler = Crawler()
# crawler.crawl(page_list)
searcher = Searcher()
searcher.getMatchRows(u'家的钟')

