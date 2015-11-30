# coding=utf-8
import hashlib
import random

import time
from django.test import Client

__author__ = 'guangchen'


class WechatClient(Client):
    def __init__(self, wechat_url='/', token='', from_user='from', to_user='to', enforce_csrf_checks=False, **defaults):
        self.wechat_url = wechat_url
        self.token = token
        self.from_user = from_user
        self.to_user = to_user
        self.msg_id = 0
        super().__init__(enforce_csrf_checks, **defaults)

    def send_wechat_text(self, content: str):
        self.msg_id += 1
        timestamp = str(int(time.time()))
        nonce = str(random.randint(1000000000, 9999999999))
        token = self.token
        group = [timestamp, nonce, token]
        group.sort()
        sha = hashlib.sha1()
        sha.update("".join(group).encode('utf-8'))
        signature = sha.hexdigest()
        template = '''<xml>
<ToUserName><![CDATA[%(to)s]]></ToUserName>
<FromUserName><![CDATA[%(from)s]]></FromUserName>
<CreateTime>%(time)s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%(content)s]]></Content>
<MsgId>%(id)s</MsgId>
</xml>'''
        data = template % {
            'to': self.to_user,
            'from': self.from_user,
            'time': timestamp,
            'content': content,
            'id': self.msg_id,
        }
        return self.post(self.wechat_url + '?signature=%s&timestamp=%s&nonce=%s' % (signature, timestamp, nonce), data=data, content_type='text/xml')

