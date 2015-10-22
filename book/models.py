# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(u"发行商名称",max_length=30)
    address = models.CharField(u"地址",max_length=50)
    city = models.CharField(u'城市',max_length=60)
    state_province = models.CharField(u"领域",max_length=30)
    country = models.CharField(u'国家',max_length=50)
    website = models.URLField()

    class Meta:
        managed = True
        db_table = 'b_publisher'
        ordering = ["-name"]
        verbose_name = u'出版商'
        verbose_name_plural = u'出版商页面'


    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    salutation = models.CharField(u'称呼',max_length=10)
    name = models.CharField(u'名字',max_length=200)
    email = models.EmailField(verbose_name="邮箱")
    #headshot = models.ImageField(upload_to='author_headshots')
    last_accessed = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'b_author'
        ordering = ["-name"]
        verbose_name = u'作者'
        verbose_name_plural = u"作者页面"


    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Book(models.Model):
    title = models.CharField(u'书名',max_length=100)
    authors = models.ManyToManyField('Author',verbose_name=u'作者',)
    publisher = models.ForeignKey(Publisher,verbose_name=u"发行商")
    publication_date = models.DateField(verbose_name=u"发布日期")

    class Meta:
        managed = True
        db_table = 'b_book'
        ordering = ["-publication_date"]
        verbose_name = u'书籍'
        verbose_name_plural = u'书籍页面'

    def  __str__(self):
        return  self.title