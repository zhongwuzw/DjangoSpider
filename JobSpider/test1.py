# -*- coding: utf-8 -*-
from JobSpider.models import WordLocation,WordList
b = WordLocation.objects.get(pk = 1)
print b.word_id.word
p = WordList.objects.get(word = u'家')
temp_dic = {}
s = set([])
for i in p.wordlocation_set.all():
    print i.id
    s.add(i.url_id.url)

    