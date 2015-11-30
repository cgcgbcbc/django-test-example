# coding=utf-8
__author__ = 'guangchen'

from django.test import TestCase
from support import WechatClient

import xml.etree.cElementTree as ET


class TestExample(TestCase):
    def setUp(self):
        self.client = WechatClient()

    def test_fetch_ticket(self):
        response = self.client.send_wechat_text('抢票')
        msg = ET.fromstring(str(response.content))
        # TODO add assert.
