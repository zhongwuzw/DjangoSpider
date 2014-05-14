from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.views.generic.list import ListView
from bs4 import BeautifulSoup
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseNotModified
from JobSpider.models import CrawlerInfo,CrawlerInfoQH
from django.core import serializers
from JobSpider.forms import UpLoadFileForm
from JobSpider.models import FileForm
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
import requests
import re

class HomePage(ListView):
    template_name = 'update_list.html'
    paginate_by = 20
#     model = CrawlerInfo
    queryset = CrawlerInfo.objects.all()
    context_object_name = 'job_list'
    
    def handleUploadedFile(self,f):
        file_path = 'E:/DjangoSpider/JobSpider/files/' + f.name
        with open(file_path,'wb+') as info:
            print f.name
            for chunk in f.chunks():
                info.write(chunk)
    
    def post(self,request,*args,**kwargs):
        form = UpLoadFileForm(request.POST,request.FILES)
        if form.is_valid():
#             self.handleUploadedFile(request.FILES['file'])
#             title = request.POST.get('title')
            title = form.cleaned_data['title']
            instance = FileForm(title = title,file = request.FILES['file'])
            instance.save()
#         return render_to_response('update_list.html')
        return HttpResponseRedirect(reverse("home_page"))
    
    def get_queryset(self):
        if self.request.GET.get('name'):
            return CrawlerInfoQH.objects.all()
        return CrawlerInfo.objects.all()
    
    def get_context_data(self,**kwargs):
        context = super(HomePage,self).get_context_data(**kwargs)
        form = UpLoadFileForm()
#         form_set = formset_factory(UpLoadFileForm,extra = 2,can_delete = True)
        if self.request.POST:
            print 'post'
        else:
            print 'get'
        self.request.session[0] = 'bar'
        print self.request.session[0]
        context['form'] = form
        context['test'] = 'test'
#         if self.request.GET.get('name'):
#             context['test_qing_hua'] = 3
        return context
    
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