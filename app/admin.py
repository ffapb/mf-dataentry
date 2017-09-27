from django.contrib import admin
from .management.commands._mfManager import MfManager
from . import models

admin.site.register(models.Currency)
admin.site.register(models.Nationality)
admin.site.register(models.SecurityShare)
admin.site.register(models.SecurityOption)
admin.site.register(models.SecurityBond)
admin.site.register(models.SecurityFutures)

