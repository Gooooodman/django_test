# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salutation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('last_accessed', models.DateTimeField()),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': '\u4f5c\u8005',
                'db_table': 'b_author',
                'managed': True,
                'verbose_name_plural': '\u4f5c\u8005\u9875\u9762',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(to='book.Author')),
            ],
            options={
                'ordering': ['-publication_date'],
                'verbose_name': '\u4e66\u7c4d',
                'db_table': 'b_book',
                'managed': True,
                'verbose_name_plural': '\u4e66\u7c4d\u9875\u9762',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': '\u51fa\u7248\u5546',
                'db_table': 'b_publisher',
                'managed': True,
                'verbose_name_plural': '\u51fa\u7248\u5546\u9875\u9762',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='book.Publisher'),
        ),
    ]
