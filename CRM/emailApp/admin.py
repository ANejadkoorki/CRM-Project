from django.contrib import admin
from . import models

# admin site header
admin.site.site_header = 'CRM System'


@admin.register(models.EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    """
        represents EmailHistory Model admin interface
    """
    list_display = [
        'id',
        'created_on',
        'sender',
        'receiver_email_address',
        'is_successful',
    ]
