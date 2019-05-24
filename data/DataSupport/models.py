# coding=utf-8
from __future__ import unicode_literals

from django.db import models

class New(models.Model):
    kind = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    pic_url = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    jianjie = models.CharField(max_length=256)
    date = models.CharField(max_length=256)
    content_url = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'新闻数据'
        verbose_name_plural = u'新闻数据'

