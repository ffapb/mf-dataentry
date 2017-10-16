from __future__ import unicode_literals
#from django.conf import settings
from django.db import models
from .management.commands._mfManager import MfManager
import yaml
import os
class MappableModel(models.Model):
    code_leb = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=10,  unique=True, null=True, blank=True)
    name     = models.CharField(max_length=100, unique=True)
    class Meta:
      abstract = True
    def __str__(self):
      codes = [
        "LB" if self.code_leb is not None else None,
        "AE" if self.code_dub is not None else None,
      ]
      codes = [c for c in codes if c is not None]
      if len(codes)>0: codes = " (" + ", ".join(codes) + ")"
      else: codes = ""
      return self.name + codes

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
    class Meta:
      verbose_name_plural = "nationalities"
      ordering = ('name', 'code_leb', 'code_dub', )



class Subtype(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )


class RateListProvider(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class Nature(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class AssetAllocation(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class Category(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class TradingCategory(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class QuotationPlace(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class TradingCenter(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

class DepositPlace(MappableModel):
    class Meta:
      ordering = ('name', 'code_leb', 'code_dub', )

# http://stackoverflow.com/questions/24192748/ddg#24192847
def getshape(d):
    if isinstance(d, dict):
        return {k:getshape(d[k]) for k in d}
    else:
        # Replace all non-dict values with None.
        return None

class Security(models.Model):
    code = models.CharField(max_length=10, unique=True)
    circular = models.CharField(max_length=4)
    designation = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    currency = models.ForeignKey(Currency)
    subtype = models.ForeignKey(Subtype)
    category = models.ForeignKey(Category)
    trading_category = models.ForeignKey(TradingCategory)
    nature = models.ForeignKey(Nature)
    trading_center = models.ForeignKey(TradingCenter)
    nationality = models.ForeignKey(Nationality, null=True, blank=True)
    #deposit_place = models.CharField(max_length=10)
    deposit_place = models.ForeignKey(DepositPlace)
    quotation_place = models.ForeignKey(QuotationPlace)
   # ratelist = models.CharField(max_length=10)
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
    mar_short_position = models.FloatField()
    mar_lng_position = models.FloatField()
    main_short_position = models.FloatField()
    main_lng_position = models.FloatField()
   
    
    class Meta:
      abstract = True

    def __str__(self):
       return self.code

    def checkAllDropdownsOnBothLebDub(self):
      if self.currency.code_leb=='':
        raise Exception("Missing currency in leb")
      if self.currency.code_dub=='':
        raise Exception("Missing currency in dub")
      if self.nationality.code_leb=='':
        raise Exception("Missing nationality in leb")
      if self.nationality.code_dub=='':
        raise Exception("Missing nationality in dub")

    def save(self, *args, **options):
      self.checkAllDropdownsOnBothLebDub()

      super(Security,self).save( *args, **options)
      dir_path = os.path.dirname(os.path.realpath(__file__))
      fn1=os.path.join(dir_path,"credentials.yml")
      both = yaml.load(open(fn1,'r'))

      # check that format is matching with credentials.yml.dist format
      fn2=os.path.join(dir_path,"credentials.yml.dist")
      expected = yaml.load(open(fn2,'r'))
      if getshape(both) != getshape(expected):
        raise Exception("credentials.yml does not match with credentials.yml.dist")

      # iterate
      for base, credentials in both.items():
        with MfManager( host=credentials['host'], port=credentials['port'], user=credentials['user'], password=credentials['password'], db=credentials['db']) as mfMan:
          mfMan.insertSecurity(self, credentials['origin'])
         

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

