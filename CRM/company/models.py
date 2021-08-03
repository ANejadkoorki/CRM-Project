from django.core.validators import FileExtensionValidator
from django.db import models
from organization import models as organmodels
from django.utils.translation import ugettext_lazy as _


class CompanyProduct(models.Model):
    """
        represents a product object from our own company
    """
    product_name = models.CharField(max_length=50, verbose_name=_('product name'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    # tax in percent
    have_tax = models.BooleanField(default=False)
    pdf_catalog = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                                   verbose_name=_('pdf catalog'), blank=True, null=True)
    image_catalog = models.ImageField(verbose_name=_('image catalog'), blank=True, null=True)
    technical_desc = models.TextField(verbose_name=_('technical description'))
    usable_for_organizations_product = models.ManyToManyField(organmodels.OrganizationsProduct,
                                                              verbose_name=_('usable for organizations product'))

    def __str__(self):
        return self.product_name
