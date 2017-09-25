from __future__ import unicode_literals
#from django.conf import settings
from django.db import models

class MappableModel(models.Model):
    code_leb = models.CharField(max_length=20,  unique=True, null=True, blank=True)
    code_dub = models.CharField(max_length=20,  unique=True, null=True, blank=True)
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
    class Meta:
      verbose_name_plural = "nationalities"
      ordering = ('name', 'code_leb', 'code_dub', )

class Security(models.Model):
    code = models.CharField(max_length=20, unique=True)
    circular = models.CharField(max_length=200)
    bank_reference = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    currency = models.ForeignKey(Currency)
    subtype = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    trading_category = models.CharField(max_length=200)
    nature = models.CharField(max_length=200)
    trading_center = models.CharField(max_length=200)
    nationality = models.ForeignKey(Nationality, null=True, blank=True)
    quotation_place = models.CharField(max_length=200)
    deposit_place = models.CharField(max_length=200)
    ratelist = models.CharField(max_length=200)
    asset_allocation = models.CharField(max_length=200)
    group_for_ledgers = models.CharField(max_length=200)
    general_ledger = models.CharField(max_length=200)
    provider_code = models.CharField(max_length=200)
    provider_ratelist = models.CharField(max_length=200)
    monitoring_type = models.CharField(max_length=200)
    multiplier_fFor_online_prices = models.CharField(max_length=200)
    isin = models.CharField(max_length=200)
    fixing = models.BooleanField(default=False)
    fix1 = models.CharField(max_length=200)
    fix2 = models.CharField(max_length=200)
    
    class Meta:
      abstract = True

    def __str__(self):
       return self.code

    def export_file(self):

       with MfManager(host=options['host'], port=options['port'], user=options['user'], password=options['password'], db=options['db']) as mfMan:
       export= mfMan.insertSecutirty()


    def save(self, *args, **kwargs):
        super(Security,self).save(*args, **kwargs)
        self.code = export_file(self.database_path)
          

#Multi Table Inheritance
#https://godjango.com/blog/django-abstract-base-class-multi-table-inheritance/   
class SecurityShare (Security):

    shareholder_number = models.BooleanField(default=False)
    show = models.BooleanField(default=False)

    def __str__(self):
       return self.code
      
class SecurityOption(Security):

    maturity_date = models.CharField(max_length=200)
    underlying_code = models.CharField(max_length=200)
    strike_place = models.CharField(max_length=200)

    def __str__(self):
       return self.code


class SecurityBond(Security):
    moody = models.CharField(max_length=200)
    fitch = models.CharField(max_length=200)
    s_and_p = models.CharField(max_length=200)
    def __str__(self):
       return self.code


class SecurityFutures(Security):
    maturity_date = models.CharField(max_length=200)
    underlying_code = models.CharField(max_length=200)
    number_of_units = models.CharField(max_length=200)
    first_notice_date = models.CharField(max_length=200)
    shareholder_number = models.BooleanField(default=False)
    show = models.BooleanField(default=False)
    def __str__(self):
       return self.code
    class Meta:
      verbose_name_plural = "security futures"

