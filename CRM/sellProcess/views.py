import weasyprint
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from organization import models as organmodels
from company import models as compmodels
from . import models
from .forms import quote_item_create_formset
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView


class AddQuote(LoginRequiredMixin, CreateView):
    """
        this view creates several QuoteItem model objects and relates them to a Quote model Object
    """
    template_name = 'sellProcess/add-quote.html'

    def get_context_data(self, **kwargs):
        # passing the formset and organizations objects to context
        formset = quote_item_create_formset(queryset=models.QuoteItem.objects.none())
        organizations = organmodels.Organization.objects.filter(expert=self.request.user)
        return {
            'formset': formset,
            'organizations': organizations,
        }

    def post(self, *args, **kwargs):
        formset = quote_item_create_formset(data=self.request.POST)
        if formset.is_valid() and self.request.POST['organization'] != '0':
            try:
                # get quote organization
                organization = organmodels.Organization.objects.get(pk=self.request.POST['organization'],
                                                                    expert=self.request.user)
                # create quote object
                quote = models.Quote.objects.create(expert=self.request.user, organization=organization)
                for form in formset:
                    form.instance.quote = quote
                    # saving each form (quote_item) to model QuoteItem
                    form.save()
                messages.success(self.request, 'Quote Created Successfully.')
                return redirect('sellProcess:add-quote')
            except:
                messages.error(self.request, 'Failed! Please Fill the Inputs Correctly.')
                return redirect('sellProcess:add-quote')
        else:
            messages.error(self.request, 'Failed! Please Fill the Inputs Correctly.')
            return redirect('sellProcess:add-quote')


class QuoteList(LoginRequiredMixin, ListView):
    """
        this view used to list quote objects and their quoteitem_sets
    """
    model = models.Quote
    template_name = 'sellProcess/quote-list.html'
    paginate_by = 3


class QuoteDetail(LoginRequiredMixin, DetailView):
    """
        this view used to show detail of a Quote model object
    """
    model = models.Quote
    template_name = 'sellProcess/quote-detail.html'


class QuotePdf(LoginRequiredMixin, DetailView):
    """
        this view used to get pdf of quote
    """
    model = models.Quote
    template_name = 'sellProcess/quote-pdf.html'

    def get(self, request, *args, **kwargs):
        normal_rendered_page = super(QuotePdf, self).get(request, *args, **kwargs)

        rendered_content = normal_rendered_page.rendered_content

        pdf = weasyprint.HTML(string=rendered_content).write_pdf()

        response = HttpResponse(pdf, content_type='application/pdf')
        return response
