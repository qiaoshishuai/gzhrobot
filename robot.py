# -*- coding=utf-8 -*-
import requests

KEY = "图灵机器人官网的apikey"

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : '机器人名',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text').encode("utf-8")
    except:
        return msg
    return msg
