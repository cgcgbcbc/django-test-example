from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def fetch_ticket(request: HttpRequest):
    return HttpResponse('成功', content_type='text/plain')
