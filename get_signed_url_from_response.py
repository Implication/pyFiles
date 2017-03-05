#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import pycurl
import certifi
import re
import json
from io import BytesIO

def get_signed_url_from_meta()
#my api key
api_key = "32185c5205d3526514d2165040672d"
url = ""
json_dict = {}
json_dict_meta = {}
signed_url  = ""
sig_id = ""
sig_id_pat = re.compile("(sig_id=)([a-zA-Z0-9]*)")
sig_str = ""
sig_pat = re.compile("(sig=)([a-zA-Z0-9]*)")
auth = {}
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL,'https://api.meetup.com/2/events?key=32185c5205d3526514d2165040672d&group_urlname=ny-tech&sign=true')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
body = body.decode('utf-8')

#parse json response
json_dict = json.loads(body)
if(json_dict):
    #get meta data
    if('meta' in json_dict):
        json_dict_meta = json_dict['meta']
else:
    print("no json response")

# get meta data dictionary from json response
if(json_dict_meta):
    if('signed_url' in json_dict_meta):
        print(json_dict_meta['signed_url'])
        signed_url = json_dict_meta['signed_url']
        s = re.search(sig_id_pat, signed_url)
        #sig_id = s.group(2)
        auth['sig_id'] = s.group(2)
        s = re.search(sig_pat, signed_url)
        auth['sig'] = s.group(2)
        print(auth)
        
else:
    print("no meta data in response")

#print(json.dumps(body, sort_keys=True, indent=4))
#print(body.decode('utf-8'))
