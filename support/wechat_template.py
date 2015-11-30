# coding=utf-8
__author__ = 'guangchen'

reply_text_template = '''<xml>
<ToUserName><![CDATA[%(to_user)s]]></ToUserName>
<FromUserName><![CDATA[%(from_user)]]></FromUserName>
<CreateTime>%(create_time)s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%(content)s]]></Content>
</xml>'''