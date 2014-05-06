# -*- coding: utf-8 -*-
from JobSpider.models import WordLocation,WordList
p = WordLocation.objects.filter(word_id_id = u'的')
print p