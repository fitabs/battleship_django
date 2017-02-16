# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='Player Name')),
            ],
        ),
        migrations.CreateModel(
            name='WinRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_win', models.PositiveIntegerField()),
                ('number_of_lose', models.PositiveIntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battle.Player')),
            ],
        ),
    ]
