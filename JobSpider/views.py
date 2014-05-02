from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.views.generic.list import ListView
from bs4 import BeautifulSoup
from django.http.response import HttpResponse
from django.http.response import HttpResponseNotModified
from JobSpider.models import CrawlerInfo
from django.core import serializers

import requests
import re

class HomePage(ListView):
    template_name = 'update_list.html'
#     paginate_by = 20
    model = CrawlerInfo
    context_object_name = 'job_list'
    
class GetLatestInfo(TemplateView):
    def get(self,request,**kwargs):
        if kwargs['id']:
            response = HttpResponse()
            response['Content-Type'] = 'text/javascript'
            response.write(serializers.serialize('json', CrawlerInfo.objects.filter(job_id__gt = kwargs['id'])))  
            return response  

class HandleCrawler(View):
    def get(self,request): 
        headers = {"X-Requested-With":"XMLHttpRequest"}
        r = requests.get('http://bbs.byr.cn/board/Job/mode/6?_uid=guest',headers = headers)
        r.encoding = 'GBK'
        soup = BeautifulSoup(r.text)
        tag_set = soup.find_all('a',attrs = {'href':re.compile('^/article/Job/\d+$')})
        url = 'http://bbs.byr.cn'
        
        for tag in tag_set:
            if tag.parent['class'][0] == 'title_9':
                pattern = re.compile('(\d+)')
                match = pattern.search(tag['href'])
                crawler_info = CrawlerInfo(url + tag['href'],tag['title'],match.group())
                crawler_info.save()

        response = HttpResponse(status = 204)
        return response