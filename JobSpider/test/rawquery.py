# -*- coding: utf-8 -*-
from django.db import connection
def myCustomSql():
    cursor = connection.cursor()
    cursor.execute("select * from jobspider_crawlerinfo where text like %s",[u'%'+u'研究'+u'%'])
    row = cursor.fetchone()
    return row,cursor.description

r,d = myCustomSql()
print r[1]
print d