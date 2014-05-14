from django.contrib.sessions.backends.db import SessionStore
import datetime
from django.contrib.sessions.models import Session
# s = SessionStore()
# s['last_login'] = 1377373373
# s.save()
# print s.session_key
s = Session.objects.all()
for t in s:
    print t.get_decoded()