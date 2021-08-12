from django.contrib.auth import get_user_model
from django.db import models
from organization import models as organmodels
from company import models as compmodels
from django_jalali.db import models as jmodels
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Quote(models.Model):
    """
        this model represents a Quote object
    """
    organization = models.ForeignKey(
        organmodels.Organization,
        on_delete=models.PROTECT,
        verbose_name=_('organization')
    )
    expert = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name=_('expert'),
    )

    created_on = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name=_('creation time')
    )

    def calculate_final_amount_payable(self):
        """
            this method calculates each quote final amount to pay
        """
        final_amount_payable = 0
        for quote_item in self.quoteitem_set.all():
            final_amount_payable += quote_item.calculate_final_price()
        return final_amount_payable

    def __str__(self):
        return f'Quote : ({self.pk}) for organization : {self.organization}'


class QuoteItem(models.Model):
    """
        this model represents a quote item object for an special quote
    """
    quote = models.ForeignKey(
        Quote,
        on_delete=models.CASCADE,
        verbose_name=_('quote')
    )
    product = models.ForeignKey(
        compmodels.CompanyProduct,
        on_delete=models.PROTECT,
        verbose_name=_('product')
    )
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    qty = models.PositiveIntegerField(default=0, verbose_name=_('qty'))
    # discount in percent
    discount = models.FloatField(default=0, verbose_name=_('discount in percent'))

    def calculate_final_price(self):
        """
            this method calculates the final price of each quote item after tax and discount calculation
        """
        # tc = total cost
        # if quote item have tax
        taxability = compmodels.CompanyProduct.objects.get(pk=self.product_id).have_tax
        if taxability:
            # tax = 9 percent
            if self.discount > 0:
                tc = ((self.qty * self.price) * 1.09)
                tc *= ((100 - self.discount) / 100)
                return tc
            else:
                tc = ((self.qty * self.price) * 1.09)
                return tc
        # if quote item doesn't have tax
        else:
            if self.discount > 0:
                tc = (self.qty * self.price)
                tc *= ((100 - self.discount) / 100)
                return tc
            else:
                tc = (self.qty * self.price)
                return tc


class FollowUp(models.Model):
    """
        this model represents a FollowUp object
    """
    description = models.TextField(verbose_name=_('Follow Up Description'))
    expert = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name=_('expert'),
    )
    organization = models.ForeignKey(
        organmodels.Organization,
        on_delete=models.CASCADE,
        verbose_name=_('For Organization'),
    )
    created_on = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation Time')
    )

    def __str__(self):
        return f"Follow Up for {self.organization} by {self.expert}"
