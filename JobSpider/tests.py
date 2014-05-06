from django.test import TestCase
from JobSpider.Component.searchengine import Crawler
page_list = ['http://www.265.com']
crawler = Crawler()
crawler.crawl(page_list)
