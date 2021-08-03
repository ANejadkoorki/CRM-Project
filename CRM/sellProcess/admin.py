from django.contrib import admin
from . import models

# admin site header
admin.site.site_header = 'CRM System'


@admin.register(models.Quote)
class CompanyProductAdmin(admin.ModelAdmin):
    """
        represents Quote Model admin interface
    """
    list_display = [
        'id',
        'organization',
        'expert',
    ]


@admin.register(models.QuoteItem)
class CompanyProductAdmin(admin.ModelAdmin):
    """
        represents QuoteItem Model admin interface
    """
    list_display = [
        'id',
        'quote',
        'product',
        'qty',
        'price',
        'discount',
    ]
