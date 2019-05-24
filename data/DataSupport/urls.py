# coding=utf-8

from django.conf.urls import url
from DataSupport.views import data_first
urlpatterns = [
    url(r'^data/',data_first),
]
