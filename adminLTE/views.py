#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lupuxiao" 

from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response,RequestContext


@login_required
def Home(request):
	return render_to_response('index.html',locals(),RequestContext(request))