from django.conf.urls import patterns, include, url
from JobSpider.views import HandleCrawler,HomePage
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoSpider.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^start/crawler/$',HandleCrawler.as_view(),name = 'start_crawler'),
    url(r'^home/$',HomePage.as_view(),name = 'home_page'),
)
