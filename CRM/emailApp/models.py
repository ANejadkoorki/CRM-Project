from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels


# Create your models here.

class EmailHistory(models.Model):
    """
        this model represents an sent email status object
    """
    created_on = jmodels.jDateTimeField(auto_now_add=True, verbose_name=_('Creation Time'))
    sender = models.ForeignKey(get_user_model(), verbose_name=_('Sender'), on_delete=models.PROTECT)
    receiver_email_address = models.EmailField(verbose_name=_('Receiver Email Address'))
    is_successful = models.BooleanField(default=False)




