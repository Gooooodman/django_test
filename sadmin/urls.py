#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lupuxiao" 

from django.conf.urls import url,patterns



urlpatterns = patterns('sadmin.views',
#assets
    url(r'^assets_list/$','assets.AssetsList',name="assetslist"),
    url(r'^create_assets/$','assets.CreateAssets',name="createassets"),
    url(r'^edit_assets/(?P<assets_id>[0-9]+)/edit/$','assets.EditAssets',name="editassets"),
    url(r'^del_assets/(?P<assets_id>[0-9]+)/del/$','assets.DelAssets',name="delassets"),
    url(r'^jquery/$','assets.jquery_1',name="jquery_1"),
    url(r'^jquery/(?P<id>[0-9]+)/$','assets.jquery_2',name="jquery_2"),
    url(r'^jquery/demo_test.txt/$','assets.jquery_3',name="jquery_3"),
    url(r'^jquery/demo_test_post.asp/$','assets.jquery_4',name="jquery_4"),
    # url(r'^ajax/(?P<id>[0-9]+)/$','assets.ajax_1',name="ajax_1"),
    url(r'^jquery/add/$','assets.add',name="add"),
    url(r'^jquery/ajax_list/$','assets.ajax_list',name="ajax_list"),
    url(r'^jquery/ajax_dict/$','assets.ajax_dict',name="ajax_dict"),
    url(r'^jquery/ajax_read_file/$','assets.ajax_read_file',name="ajax_read_file"),
)

