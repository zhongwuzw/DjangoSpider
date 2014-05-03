from django.db import models
from django.contrib import admin

class CrawlerInfo(models.Model):
    url = models.URLField(primary_key = True)
    text = models.CharField(max_length = 255)
    job_id = models.IntegerField()
    
    class Meta:
        ordering = ['-job_id']
    
    def __unicode__(self):
        return "%s %s %s" %(self.url,self.text,self.job_id)
    
admin.site.register(CrawlerInfo)

class CrawlerInfoQH(models.Model):
    url = models.URLField(primary_key = True)
    text = models.CharField(max_length = 255)
    job_id = models.IntegerField()
    
    class Meta:
        ordering = ['-job_id']
    
    def __unicode__(self):
        return "%s %s %s" %(self.url,self.text,self.job_id)
    
admin.site.register(CrawlerInfoQH)