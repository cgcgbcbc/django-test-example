import time

from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from app.models import Activity, Ticket
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


@transaction.atomic()
def fetch_ticket(user: str) -> str:
    activity = Activity.objects.select_for_update().get()
    if activity.remain_ticket > 0:
        activity.remain_ticket -= 1
        activity.save()
        ticket = Ticket.objects.create(activity=activity, user=user)
        ticket.save()
        return '成功'
    else:
        return '失败'


@csrf_exempt
def wechat_handler(request: HttpRequest):
    data = ET.fromstring(request.body.decode())
    content = data.findtext('Content')
    from_user_name = data.findtext('FromUserName')
    if content == '抢票':
        return HttpResponse(TEXT_TPL % {
            'content': fetch_ticket(from_user_name),
            'from_user_name': 'from',
            'to_user_name': from_user_name,
            'create_time': time.time(),
        }, content_type='text/xml')
    return HttpResponse('<xml></xml>', content_type='text/xml')
