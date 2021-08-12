from django.contrib import admin
from . import models


@admin.register(models.OrganizationsProduct)
class OrganizationsProductAdmin(admin.ModelAdmin):
    """
        represents Organizations Product Model admin interface
    """
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(models.Organization)
class Organization(admin.ModelAdmin):
    """
        represents Organizations Model admin interface
    """
    list_display = [
        'id',
        'organization_name',
        'province',
        'telephone',
        'representative_full_name',
        'representative_email',
        'expert',
    ]

    list_display_links = [
        'id',
        'organization_name',
    ]

    list_editable = [
        'telephone',
        'representative_full_name',
        'representative_email',
    ]

    search_fields = [
        'organization_name',
        'province',
        'representative_full_name',
        'expert__username__icontains',
    ]
    list_filter = [
        'province',
        'manufactured_product',
        'expert',
    ]
