# -*- coding: utf-8 -*-
from JobSpider.models import WordLocation,WordList
b = WordLocation.objects.get(pk = 1)
print b.word_id.word
p = WordList.objects.get(word = u'家')
print p.wordlocation_set.all()