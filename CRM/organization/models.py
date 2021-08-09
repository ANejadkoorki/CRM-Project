from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import ugettext_lazy as _

# here is the regex validators for iranian Landline and phone number.
landline_phone_regex = RegexValidator(regex='^0[0-9]{2,}[0-9]{7,}$', message=_('This Landline number is Invalid.'))
Phone_number_regex = RegexValidator(regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}',
                                    message=_('This Phone number is Invalid.'))


class OrganizationsProduct(models.Model):
    """
        represents an product that manufactured in organizations
    """
    name = models.CharField(max_length=50, verbose_name=_('Product name'))

    def __str__(self):
        return self.name


class Organization(models.Model):
    """
        represents an organization object contains organization`s characteristics
    """
    province = models.CharField(max_length=20, verbose_name=_('Province'))
    organization_name = models.CharField(max_length=50, verbose_name=_('Organization name'), unique=True)
    telephone = models.CharField(validators=[landline_phone_regex], max_length=11,
                                 verbose_name=_('Organization telephone'))
    workers_qty = models.PositiveIntegerField(default=1, verbose_name=_('Workers Quantity'))
    manufactured_product = models.ManyToManyField(OrganizationsProduct, verbose_name=_('Manufactured product'))
    representative_full_name = models.CharField(max_length=80, verbose_name=_('Representative fullname'))
    representative_phone_number = models.CharField(validators=[Phone_number_regex], max_length=11,
                                                   verbose_name=_('Representative phone number'))
    representative_email = models.EmailField(verbose_name=_('Representative email'))
    created_on = jmodels.jDateTimeField(auto_now_add=True, verbose_name=_('Creation time'))
    expert = models.ForeignKey(get_user_model(), verbose_name=_('Expert'), on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.organization_name}'

    class Meta:
        unique_together = [
            'organization_name',
            'expert'
        ]
