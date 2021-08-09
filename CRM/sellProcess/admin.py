from django.contrib import admin
from . import models

# admin site header
admin.site.site_header = 'CRM System'


@admin.register(models.Quote)
class QuoteAdmin(admin.ModelAdmin):
    """
        represents Quote Model admin interface
    """
    list_display = [
        'id',
        'organization',
        'expert',
    ]


@admin.register(models.QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    """
        represents QuoteItem Model admin interface
    """
    list_display = [
        'id',
        'quote',
        'product',
        'qty',
        'discount',
    ]


@admin.register(models.FollowUp)
class FollowUpAdmin(admin.ModelAdmin):
    """
        represents FollowUp Model admin interface
    """
    list_display = [
        'id',
        'organization',
        'expert',
        'description',
        'created_on',
    ]

    list_display_links = [
        'organization'
    ]
