#-*- coding:utf-8 -*-
import web
import os
import hashlib
import time

class WechatInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        data = web.input()
        signature = data.signature#后台认证签名
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = 'token'

        l = [token, timestamp, nonce]
        l.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, l)
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr



















