#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lupuxiao"

from django.conf.urls import url,patterns
from book.views import PublisherList,PublisherBookList


urlpatterns = patterns('sadmin.views',
#book
    url(r'^publishers/$', PublisherList.as_view(),name="publisherlist"),
    url(r'^book_by_publishers/$', PublisherBookList.as_view(),name="publisherbooklist"),
)

