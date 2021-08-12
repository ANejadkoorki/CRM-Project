from django.contrib import admin
from django.utils.translation import ugettext as _
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

    list_display_links = [
        'id',
        'organization',
    ]

    search_fields = [
        'organization__organization_name__icontains',
        'expert__username__icontains',
    ]

    list_filter = [
        'expert',
    ]


@admin.register(models.QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    """
        represents QuoteItem Model admin interface
    """
    list_display = [
        'id',
        'product',
        'quote',
        'price',
        'qty',
        'discount',
    ]

    list_display_links = [
        'id',
        'product',
    ]

    list_editable = [
        'qty',
        'discount',
    ]

    search_fields = [
        'product__product_name__icontains',
        'quote__organization__organization_name__icontains',
    ]

    list_filter = [
        'quote',
    ]

    @admin.action(description=_('Set discount to 0'))
    def set_discount_to_zero(modeladmin, request, queryset):
        queryset.update(discount=0.0)

    actions = [
        set_discount_to_zero,
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
        'id',
        'organization',
    ]

    search_fields = [
        'organization__organization_name__icontains',
        'expert__username__icontains',
    ]

    list_filter = [
        'organization',
        'expert',
    ]


