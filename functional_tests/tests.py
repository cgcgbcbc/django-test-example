# coding=utf-8
__author__ = 'guangchen'

from django.test import TestCase
from support import WechatClient

import xml.etree.cElementTree as ET


class TestExample(TestCase):
    def setUp(self):
        self.client = WechatClient(wechat_url='/wechat/')

    def test_fetch_ticket(self):
        response = self.client.send_wechat_text('抢票')
        self.assertEqual(response.status_code, 200)
        msg = ET.fromstring(response.content.decode())
        # TODO add assert.
