from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
from app.models import Activity


def fetch_ticket(request: HttpRequest):
    activity = Activity.objects.get()
    if activity.remain_ticket > 0:
        activity.remain_ticket -= 1
        activity.save()
        return HttpResponse('成功', content_type='text/plain')
    else:
        return HttpResponse('失败', content_type='text/plain')
