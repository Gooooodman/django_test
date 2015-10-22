#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lupuxiao" 

from django import forms
from .models import Assets

#资产
class AssetsListForm(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ['type','name','config_time','bill','status','recipients','config_mod','scrap']








