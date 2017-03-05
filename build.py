def build(url)
{
    buffer = BytesIO();
    c = pycurl.Curl()
    c = setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.WRITEDATA, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    body = body.decode('utf-8')
    json_dict = json.loads(body)
    rslts_list = json_dict['results']
    return rslts_list
}
