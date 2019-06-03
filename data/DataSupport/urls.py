# coding=utf-8

from django.conf.urls import url
from DataSupport.views import *
urlpatterns = [
    url(r'^qiyeyaowen/',qiyeyaowen),
    url(r'^yiliaoxinwen/',yiliaoxinwen),
    url(r'^shenghuotieshi/',shenghuotieshi),
    url(r'^yaopinxinwen/',yaopinxinwen),
    url(r'^shehuiredian/',shehuiredian),
]
