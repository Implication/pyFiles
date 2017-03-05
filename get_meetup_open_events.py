#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import pycurl
import certifi
import re
import json
import datetime
from io import BytesIO

f1 = open('open_events.txt','w')
f2 = open('event_fields.txt','w')

base_url = "'https://api.meetup.com"
api = "/2/open_events?"
api_key = "32185c5205d3526514d2165040672d"
api_key_params = "key=" + api_key + "&sign=true"
urlkey = "board-games"
lon = ""
lat = ""
zip = "92679"
json_dict = {}

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL,'https://api.meetup.com/2/open_events?tdesc=true&topic=board-games&zip=92679&key=32185c5205d3526514d2165040672d&sign=true')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
body = body.decode('utf-8')
json_dict = json.loads(body)
rslts_list = json_dict['results']

#loop through local events
for evnt in rslts_list:   
    event_dict = evnt
    
    #convert  UTC from epoch to date time
    event_dict['time'] = str(datetime.datetime.fromtimestamp(event_dict['time']/1000).strftime('%c'))
    
    #if no venue set, set to 'become member'
    if('venue' in event_dict):
        print(event_dict['venue'])
    else:
        event_dict['venue'] = "must be member to join to see venue"
        
    print(event_dict['name']+" : "+event_dict['status'] + " : " + event_dict['time'] + " : " + str(event_dict['venue']), file=f1)

    #for info in event_dict:
       # print(info, file = f2)
#    event_dict = rslts_dict[evnt]
#    print(event_dict)
    #for details in event_dict:
      #  print(details)
#cats_lst = json_dict['results']

#for cat in cats_lst:

#    print(cat, file=f1)
#print(result_dict)[i]