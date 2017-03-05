#! /usr/bin/env python
import re

def get_signed_url_from_meta(json_dict_meta):
    #my api key
    json_dict = {}
    json_dict_meta = {}
    signed_url  = ""
    sig_id = ""
    sig_id_pat = re.compile("(sig_id=)([a-zA-Z0-9]*)")
    sig_str = ""
    sig_pat = re.compile("(sig=)([a-zA-Z0-9]*)")
    signed_url_dict = {}

    #get signed_url data from meta data
    if(json_dict_meta):
        if('signed_url' in json_dict_meta):
            signed_url = json_dict_meta['signed_url']
            if(signed_url):
                s = re.search(sig_id_pat, signed_url)
                signed_url_dict['sig_id'] = s.group(2)
                s = re.search(sig_pat, signed_url)
                signed_url_dict['sig'] = s.group(2)

                print(json_dict_meta['signed_url'])
                print(signed_url_dict)
                return signed_url_dict
            else:
                return None
        else:
            return None
    else:
        print("no meta data in response")
        return None
