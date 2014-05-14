#coding=utf8
from django import forms

class UpLoadFileForm(forms.Form):
    title = forms.CharField(max_length = 50,label = u'标题')
    file = forms.FileField(label = u'文件浏览')
    time = forms.DateField()