from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Organization
        fields = (
            'pk',
            'province',
            'organization_name',
            'telephone',
            'workers_qty',
            'manufactured_product',
            'representative_full_name',
            'representative_phone_number',
            'representative_email',
            'created_on',
            'expert',
        )
        read_only_fields = (
            'pk',
        )


class OrganizationsProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OrganizationsProduct
        fields = (
            'pk',
            'name',
        )
        read_only_fields = (
            'pk',
        )
