import time
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Activity
import xml.etree.cElementTree as ET


TEXT_TPL = '''
<xml>
<ToUserName><![CDATA[%(to_user_name)s]]></ToUserName>
<FromUserName><![CDATA[%(from_user_name)s]]></FromUserName>
<CreateTime>%(create_time)d</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%(content)s]]></Content>
</xml>
'''


def fetch_ticket(request: HttpRequest) -> HttpResponse:
    activity = Activity.objects.get()
    if activity.remain_ticket > 0:
        activity.remain_ticket -= 1
        activity.save()
        return HttpResponse('成功', content_type='text/plain')
    else:
        return HttpResponse('失败', content_type='text/plain')


def wechat_handler(request: HttpRequest):
    data = ET.fromstring(request.body.decode())
    content = data.findtext('Content')
    from_user_name = data.findtext('FromUserName')
    if content == '抢票':
        return HttpResponse(TEXT_TPL % {
            'content': fetch_ticket(request).content.decode(),
            'from_user_name': 'from',
            'to_user_name': from_user_name,
            'create_time': time.time(),
        }, content_type='text/xml')
    return HttpResponse('<xml></xml>', content_type='text/xml')
