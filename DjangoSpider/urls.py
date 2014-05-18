from django.conf.urls import patterns, include, url
from JobSpider.views import HandleCrawler,HomePage,GetLatestInfo,Login,Logout,CsvTest
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoSpider.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^start/crawler/$',HandleCrawler.as_view(),name = 'start_crawler'),
    url(r'^home/$',HomePage.as_view(),name = 'home_page'),
    url(r'^get/updates/(?P<id>\d+)/$',GetLatestInfo.as_view(),name = 'get_latest_info'),
    url(r'^login/$',Login.as_view(),name = 'login'),
    url(r'^logout/$',Logout.as_view(),name = 'logout'),
    url(r'csvtest/$',CsvTest.as_view(),name = 'csvtest'),
)
