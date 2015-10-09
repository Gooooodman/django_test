# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('config_time', models.DateField(verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('bill', models.CharField(default=b'Y', max_length=3, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe5\x8f\x91\xe7\xa5\xa8', choices=[(b'Y', b'\xe6\x9c\x89\xe5\x8f\x91\xe7\xa5\xa8'), (b'N', b'\xe6\x97\xa0\xe5\x8f\x91\xe7\xa5\xa8')])),
                ('status', models.CharField(max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('recipients', models.CharField(max_length=20, verbose_name=b'\xe9\xa2\x86\xe7\x94\xa8\xe6\x83\x85\xe5\x86\xb5')),
                ('config_mod', models.CharField(max_length=20, verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe6\x9b\xb4\xe6\x94\xb9')),
                ('scrap', models.CharField(default=b'N', max_length=3, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8a\xa5\xe5\xba\x9f', choices=[(b'Y', b'\xe6\x8a\xa5\xe5\xba\x9f'), (b'N', b'\xe6\x9c\xaa\xe6\x8a\xa5\xe5\xba\x9f')])),
            ],
            options={
                'ordering': ['-config_time'],
                'verbose_name': '\u8d44\u4ea7',
                'verbose_name_plural': '\u8d44\u4ea7\u5217\u8868',
            },
        ),
    ]
