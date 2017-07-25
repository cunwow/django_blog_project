from django.shortcuts import render
from djang.http import HttpResponse

def index(request):
    return HttpResponse("欢迎访问我的博客首页！")

