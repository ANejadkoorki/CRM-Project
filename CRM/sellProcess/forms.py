from . import models
from django.forms import modelformset_factory

quote_item_create_formset = modelformset_factory(models.QuoteItem, fields=(
    'product',
    'qty',
    'discount',
))

