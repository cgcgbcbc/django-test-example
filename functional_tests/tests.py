# coding=utf-8

from django.test import TestCase
from support import WechatClient
import xml.etree.cElementTree as ET

__author__ = 'guangchen'


class TestExample(TestCase):
    fixtures = ['activity.yaml']

    def setUp(self):
        self.client = WechatClient(wechat_url='/wechat/')

    def test_fetch_ticket(self):
        response = self.client.send_wechat_text('抢票')
        self.assertEqual(response.status_code, 200)
        msg = ET.fromstring(response.content.decode())
        msg_content = msg.findtext('Content')
        self.assertEqual(msg_content, '成功')
