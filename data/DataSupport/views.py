# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataSupport.models import New
from function import to_dict


def data_first(request):
    data = New.objects.filter(kind="企业要闻")
    x = []
    for i in data:
        a = {"kind": i.kind, "title": i.title, "pic_url": i.pic_url,
             "author": i.author, "date": i.date, "jianjie": i.jianjie,
             "content_url": i.content_url}
        x.append(a)
    return JsonResponse(x, safe=False)
