# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 02:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RssPost',
            new_name='Post',
        ),
    ]
