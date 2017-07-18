# -*- coding:utf-8 -*-

import requests
import json

def talk(content):
    url = 'http://www.tuling123.com/openapi/api'
    s = requests.session()
    d = {'key': '064162a25b7f4e819238e753839e7f32', 'info': content}
    data = json.dumps(d)
    r = s.post(url, data=data)
    text = json.loads(r.text)
    return text['text']

#print talk('我爱你')

