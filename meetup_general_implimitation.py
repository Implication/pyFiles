
def buff(str){
    buffer = BytestIO()
    c = pycurl.Curl()
    c = setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    }

def buildurl(){
    base = "http://api.meetup.com"
    api = "2/open_events?"
    api_key = "24607d712f7b134f5d4f7257430364d"
    api_key_params = 'key=' + api_key + 'sign=true'
    lon = ""
    lat = ""
    zip = "92679"
    json_dict{}
    }
