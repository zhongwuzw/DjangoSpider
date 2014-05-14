#coding=utf8
from django import forms

class UpLoadFileForm(forms.Form):
    title = forms.CharField(max_length = 50)
    file = forms.FileField()