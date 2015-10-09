# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models

# Create your models here.

class Assets(models.Model):
    scrap_choices = (
        ('Y', "报废"),
        ('N', "未报废"),
    )
    bill_choices = (
        ('Y', "有发票"),
        ('N', "无发票"),
    )

    type = models.CharField("类型",max_length=20)
    name = models.CharField("名称",max_length=50)
    config_time = models.DateField(blank=True,verbose_name="配置时间")
    bill = models.CharField(max_length=3,choices=bill_choices,default="Y",verbose_name="是否有发票")
    status = models.CharField("状态",max_length=20)
    recipients = models.CharField("领用情况",max_length=20)
    config_mod = models.CharField("配置更改",max_length=20)
    scrap = models.CharField(max_length=3,choices=scrap_choices,default="N",verbose_name="是否报废")

    def __str__(self):
        return u'%s - %s - %s' %(self.type, self.name, self.config_time )

    class Meta:
        verbose_name = u'资产'
        verbose_name_plural = u'资产列表'
        ordering = ['-config_time']







