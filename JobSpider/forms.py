#coding=utf8
from django import forms
from django.forms.extras.widgets import SelectDateWidget

BIRTH_YEAR_CHOICES  = ('1980','1981','1982')

class UpLoadFileForm(forms.Form):
    title = forms.CharField(max_length = 50,label = u'标题')
    file = forms.FileField(label = u'文件浏览')
    time = forms.DateField(widget = SelectDateWidget(years = BIRTH_YEAR_CHOICES))