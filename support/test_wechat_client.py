# coding=utf-8
from unittest import TestCase
from unittest.mock import patch

from support.wechat_client import WechatClient

__author__ = 'guangchen'


class TestWechatClient(TestCase):
    def setUp(self):
        self.client = WechatClient(token='abc')

    def test_send_wechat_text(self):
        self.assertIn('send_wechat_text', self.client.__dir__(), 'WechatClient has send_wechat_text attr')
        self.assertTrue(hasattr(self.client.__getattribute__('send_wechat_text'), '__call__'))

        with patch.object(self.client, 'post') as mock_post, patch('time.time') as mock_time, patch('random.randint') as mock_random:
            mock_time.return_value = 1448898595
            mock_random.return_value = 1628484290
            self.client.send_wechat_text('test')
            mock_post.assert_called_once_with(
                '/?signature=d6e9aec062e5e5e73f847529f4162f10bd7c927c&timestamp=1448898595&nonce=1628484290',
data='''<xml>
<ToUserName><![CDATA[to]]></ToUserName>
<FromUserName><![CDATA[from]]></FromUserName>
<CreateTime>1448898595</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[test]]></Content>
<MsgId>1</MsgId>
</xml>''', content_type='text/xml')