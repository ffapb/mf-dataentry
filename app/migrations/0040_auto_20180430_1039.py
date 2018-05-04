# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-30 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20171016_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitybond',
            name='bloomberg_code',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='securityfutures',
            name='bloomberg_code',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='securityoption',
            name='bloomberg_code',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='securityshare',
            name='bloomberg_code',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
