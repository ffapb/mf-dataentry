from __future__ import unicode_literals
#from django.conf import settings
from django.db import models
from .management.commands._mfManager import MfManager
import yaml
import os
class MappableModel(models.Model):
    code_leb = models.CharField(max_length=2,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=2,  unique=True, null=True, blank=True)
    name     = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    class Meta:
      abstract = True

    # https://stackoverflow.com/a/15534514/4126114
    def save(self, *args, **kwargs):
      if self.code_leb == "": self.code_leb = None
      if self.code_dub == "": self.code_dub = None
      super(MappableModel, self).save(*args, **kwargs)

class Currency(MappableModel):
    class Meta:
      verbose_name_plural = "currencies"
      ordering = ('name', 'code_leb', 'code_dub', )

class Nationality(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      verbose_name_plural = "nationalities"

      ordering = ('name', 'code_leb', 'code_dub', )



class Subtype(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      verbose_name_plural = "subtypes"

      ordering = ('name', 'code_leb', 'code_dub', )


class RateListProvider(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class Nature(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class AssetAllocation(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class Category(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class TradingCategory(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class QuotationPlace(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class TradingCenter(MappableModel):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class Security(models.Model):
    code = models.CharField(max_length=20, unique=True)
    circular = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency)
    subtype = models.ForeignKey(Subtype)
    category = models.ForeignKey(Category)
    trading_category = models.ForeignKey(TradingCategory)
    nature = models.ForeignKey(Nature)
    trading_center = models.ForeignKey(TradingCenter)
    nationality = models.ForeignKey(Nationality, null=True, blank=True)
    quotation_place = models.CharField(max_length=10)
    deposit_place = models.ForeignKey(QuotationPlace)
    ratelist = models.CharField(max_length=10)
    asset_allocation = models.ForeignKey(AssetAllocation)
    group_for_ledgers = models.CharField(max_length=200)
    general_ledger = models.CharField(max_length=4)
    provider_code = models.CharField(max_length=50)
    provider_ratelist = models.ForeignKey(RateListProvider)
   # monitoring_type = models.IntegerField()
    multiplier_for_online_prices = models.IntegerField()
    isin = models.CharField(max_length=20)
    fixing = models.BooleanField(default=False)
    fix1 = models.CharField(max_length=5)
    fix2 = models.CharField(max_length=5)
    mar_short_position = models.CharField(max_length=5)
    mar_lng_position = models.CharField(max_length=5)
    main_short_position = models.CharField(max_length=5)
    main_lng_position = models.CharField(max_length=5)
    
   
   
    
    class Meta:
      abstract = True

    def __str__(self):
       return self.code


    def save(self, *args, **options):
      super(Security,self).save( *args, **options)
      dir_path = os.path.dirname(os.path.realpath(__file__))
      fn=os.path.join(dir_path,"credentials.yml")
      credentials = yaml.load(open(fn,'r'))
      with MfManager(host=credentials['host'], port=credentials['port'], user=credentials['user'], password=credentials['password'], db=credentials['db']) as mfMan:
           mfMan.insertSecurity(self)
  

#Multi Table Inheritance
#https://godjango.com/blog/django-abstract-base-class-multi-table-inheritance/   
class SecurityShare (Security):

    shareholder_number = models.BooleanField(default=False)
    show = models.BooleanField(default=False)

    def __str__(self):
       return self.code
      
class SecurityOption(Security):

    maturity_date = models.DateTimeField()
    underlying_code = models.CharField(max_length=10)
    strike_place = models.FloatField()

    def __str__(self):
       return self.code


class SecurityBond(Security):
    moody = models.CharField(max_length=100)
    fitch = models.CharField(max_length=100)
    s_and_p = models.CharField(max_length=100)
    def __str__(self):
       return self.code


class SecurityFutures(Security):
    maturity_date = models.DateTimeField()
    underlying_code = models.CharField(max_length=10)
    number_of_units = models.IntegerField()
    first_notice_date = models.DateTimeField()
    shareholder_number = models.BooleanField(default=False)
    show = models.BooleanField(default=False)
    def __str__(self):
       return self.code
    class Meta:
      verbose_name_plural = "security futures"

