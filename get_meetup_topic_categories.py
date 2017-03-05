#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import pycurl
import certifi
import re
import json
from io import BytesIO

f1 = open('topic_categories.txt','w')

api_key = "32185c5205d3526514d2165040672d"
url = ""
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL,'https://api.meetup.com/2/topic_categories?key=32185c5205d3526514d2165040672d&sign=true')

c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
body = body.decode('utf-8')
json_dict = json.loads(body)
cats_lst = json_dict['results']

for cat in cats_lst:
    print(cat, file=f1)
#print(result_dict)[i]