# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20171012_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='securitybond',
            name='quotation_place',
        ),
        migrations.RemoveField(
            model_name='securityfutures',
            name='quotation_place',
        ),
        migrations.RemoveField(
            model_name='securityoption',
            name='quotation_place',
        ),
        migrations.RemoveField(
            model_name='securityshare',
            name='quotation_place',
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='asset_allocation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='multiplier_for_online_prices',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='nature',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='provider_ratelist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='trading_category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='trading_center',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='asset_allocation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='multiplier_for_online_prices',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='nature',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='provider_ratelist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='trading_category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='trading_center',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='asset_allocation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='multiplier_for_online_prices',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='nature',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='provider_ratelist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='trading_category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='trading_center',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='asset_allocation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='multiplier_for_online_prices',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='nature',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='provider_ratelist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='trading_category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='trading_center',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='AssetAllocation',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Nature',
        ),
        migrations.DeleteModel(
            name='QuotationPlace',
        ),
        migrations.DeleteModel(
            name='RateListProvider',
        ),
        migrations.DeleteModel(
            name='TradingCategory',
        ),
        migrations.DeleteModel(
            name='TradingCenter',
        ),
    ]