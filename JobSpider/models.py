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

class UrlList(models.Model):
    url = models.URLField(primary_key = True)
    
    def __unicode__(self):
        return u"%s" % self.url
    
admin.site.register(UrlList)

class WordList(models.Model):
    word = models.CharField(max_length = 1,primary_key = True)
    
    def __unicode__(self):
        return u"%s" % self.word
    
admin.site.register(WordList)

class Link(models.Model):
    from_id = models.URLField()
    to_id = models.URLField()
    
    def __unicode__(self):
        return u"From %s to %s" % (self.from_id,self.to_id)
    
admin.site.register(Link)

class LinkWords(models.Model):
    word_id = models.ForeignKey(WordList)
    link_id = models.ForeignKey(Link)
    
    def __unicode__(self):
        return "u%s,%s" % (self.word_id,self.link_id)
    
admin.site.register(LinkWords)

class WordLocation(models.Model):
    url_id = models.ForeignKey(UrlList)
    word_id = models.ForeignKey(WordList)
    location = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return u"%s,%s,%s" % (self.url_id,self.word_id,self.location)
    
admin.site.register(WordLocation)