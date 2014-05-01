import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoSpider.settings'

sys.path.append('E:/DjangoSpider')
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()