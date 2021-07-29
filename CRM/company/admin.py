from django.contrib import admin
from django.utils.translation import ugettext as _
from . import models

# admin site header
admin.site.site_header = 'CRM System'


@admin.register(models.CompanyProduct)
class CompanyProductAdmin(admin.ModelAdmin):
    """
        represents Company Product Model admin interface
    """
    list_display = [
        'id',
        'product_name',
        'price',
        'have_tax',
    ]

    list_display_links = [
        'id',
        'product_name',
    ]

    search_fields = [
        'product_name',
    ]

    list_filter = [
        'usable_for_organizations_product',
        'have_tax',
    ]

    # Actions :

    @admin.action(description=_('Set to taxable'))
    def set_to_have_tax(modeladmin, request, queryset):
        queryset.update(have_tax=True)

    @admin.action(description=_('Exempt from taxation'))
    def set_to_exempt_tax(modeladmin, request, queryset):
        queryset.update(have_tax=False)

    actions = [
        set_to_have_tax,
        set_to_exempt_tax,
    ]
