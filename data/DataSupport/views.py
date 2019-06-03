# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataSupport.models import New
from function import to_dict


def qiyeyaowen(request):
    data = New.objects.filter(kind="企业要闻")
    x = []
    for i in data:
        a = {"kind": i.kind, "title": i.title, "pic_url": i.pic_url,
             "author": i.author, "date": i.date, "jianjie": i.jianjie,
             "content_url": i.content_url}
        x.append(a)
    return JsonResponse(x, safe=False)


def yiliaoxinwen(request):
    data = New.objects.filter(kind="医疗新闻")
    x = []
    for i in data:
        a = {"kind": i.kind, "title": i.title, "pic_url": i.pic_url,
             "author": i.author, "date": i.date, "jianjie": i.jianjie,
             "content_url": i.content_url}
        x.append(a)
    return JsonResponse(x, safe=False)


def shenghuotieshi(request):
    data = New.objects.filter(kind="生活贴士")
    x = []
    for i in data:
        a = {"kind": i.kind, "title": i.title, "pic_url": i.pic_url,
             "author": i.author, "date": i.date, "jianjie": i.jianjie,
             "content_url": i.content_url}
        x.append(a)
    return JsonResponse(x, safe=False)


def yaopinxinwen(request):
    data = New.objects.filter(kind="药品新闻")
    x = []
    for i in data:
        a = {"kind": i.kind, "title": i.title, "pic_url": i.pic_url,
             "author": i.author, "date": i.date, "jianjie": i.jianjie,
             "content_url": i.content_url}
        x.append(a)
    return JsonResponse(x, safe=False)


def shehuiredian(request):
    data = New.objects.filter(kind="社会热点")
    x = []
    for i in data:
        a = {"kind": i.kind, "title": i.title, "pic_url": i.pic_url,
             "author": i.author, "date": i.date, "jianjie": i.jianjie,
             "content_url": i.content_url}
        x.append(a)
    return JsonResponse(x, safe=False)
