from django.contrib import admin
from .models import Asset, Maintenance, Inventory

admin.site.register(Asset)
admin.site.register(Maintenance)
admin.site.register(Inventory)
