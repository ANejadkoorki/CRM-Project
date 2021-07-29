from django import forms
from . import models


class OrganizationForm(forms.ModelForm):
    """
        represents a model form to get organization detail and create \
        an Organization model object with them
    """
    class Meta:
        model = models.Organization
        fields = (
            'province',
            'organization_name',
            'telephone',
            'workers_qty',
            'manufactured_product',
            'representative_full_name',
            'representative_phone_number',
            'representative_email',
        )
