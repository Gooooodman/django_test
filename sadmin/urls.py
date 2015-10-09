#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lupuxiao" 

from django.conf.urls import url,patterns
from sadmin import views


urlpatterns = patterns('sadmin.views',
#assets
    url(r'^assets_list/$','assets.AssetsList',name="assetslist"),
    url(r'^create_assets/$','assets.CreateAssets',name="createassets"),
    url(r'^edit_assets/(?P<assets_id>[0-9]+)/edit/$','assets.EditAssets',name="editassets"),
    url(r'^del_assets/(?P<assets_id>[0-9]+)/del/$','assets.DelAssets',name="delassets"),

)

