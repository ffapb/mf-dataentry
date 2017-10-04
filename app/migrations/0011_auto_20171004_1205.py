# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20171004_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitybond',
            name='main_lng_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securitybond',
            name='main_short_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securitybond',
            name='mar_lng_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securitybond',
            name='mar_short_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityfutures',
            name='main_lng_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityfutures',
            name='main_short_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityfutures',
            name='mar_lng_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityfutures',
            name='mar_short_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityoption',
            name='main_lng_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityoption',
            name='main_short_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityoption',
            name='mar_lng_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityoption',
            name='mar_short_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityshare',
            name='main_lng_position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityshare',
            name='main_short_position',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityshare',
            name='mar_lng_position',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securityshare',
            name='mar_short_position',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
