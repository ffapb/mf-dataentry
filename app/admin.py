from django.contrib import admin
from .management.commands._mfManager import MfManager
from . import models

admin.site.register(models.Currency)
admin.site.register(models.Nationality)
admin.site.register(models.Subtype)
admin.site.register(models.SecurityShare)
admin.site.register(models.SecurityOption)
admin.site.register(models.SecurityBond)
admin.site.register(models.SecurityFutures)
admin.site.register(models.RateListProvider)
admin.site.register(models.Nature)
admin.site.register(models.AssetAllocation)
admin.site.register(models.Category)
admin.site.register(models.TradingCategory)
admin.site.register(models.QuotationPlace)
admin.site.register(models.TradingCenter)
admin.site.register(models.DepositPlace)
admin.site.register(models.Titre)
