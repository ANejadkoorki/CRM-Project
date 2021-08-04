from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from organization import models as organmodels
from company import models as compmodels
from . import models
from .forms import quote_item_create_formset
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView


class AddQuote(LoginRequiredMixin, CreateView):
    """
        this view creates several QuoteItem model objects and relates them to a Quote model Object
    """
    template_name = 'sellProcess/add-quote.html'

    def get_context_data(self, **kwargs):
        formset = quote_item_create_formset(queryset=models.QuoteItem.objects.none())
        organizations = organmodels.Organization.objects.filter(expert=self.request.user)
        return {
            'formset': formset,
            'organizations': organizations,
        }

    def post(self, *args, **kwargs):
        formset = quote_item_create_formset(data=self.request.POST)
        if formset.is_valid() and self.request.POST['organization'] is None:
            organization = organmodels.Organization.objects.get(pk=self.request.POST['organization'],
                                                                expert=self.request.user)
            quote = models.Quote.objects.create(expert=self.request.user, organization=organization)
            for form in formset:
                form.instance.quote = quote
                form.save()
            messages.success(self.request, 'Quote Created Successfully.')
            return redirect('sellProcess:add-quote')
        else:
            messages.error(self.request, 'Failed! Please Fill the Inputs Correctly.')
            return redirect('sellProcess:add-quote')


