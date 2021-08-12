import weasyprint
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from organization import models as organmodels
from company import models as compmodels
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from . import models
from .forms import quote_item_create_formset
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView


@method_decorator(csrf_exempt, name='dispatch')
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

                    # get quote item product price
                    cleaned_data = form.cleaned_data
                    price = cleaned_data.get('product').price
                    form.instance.price = price

                    # saving each form (quote_item) to model QuoteItem
                    form.save()
                messages.success(self.request, _('Quote Created Successfully.'))
                return redirect('sellProcess:add-quote')
            except:
                messages.error(self.request, _('Failed! Please Fill the Inputs Correctly.'))
                return redirect('sellProcess:add-quote')
        else:
            messages.error(self.request, _('Failed! Please Fill the Inputs Correctly.'))
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

        pdf = weasyprint.HTML(string=rendered_content, base_url='http://127.0.0.1:8000').write_pdf()

        response = HttpResponse(pdf, content_type='application/pdf')
        return response


@method_decorator(csrf_exempt, name='dispatch')
class FollowUpView(LoginRequiredMixin, CreateView):
    """
        this view used to create a FollowUp model object
    """
    model = models.FollowUp
    template_name = 'sellProcess/follow-up.html'
    fields = (
        'description',
    )

    def form_valid(self, form):
        # filling the FollowUp model`s expert field with request.user
        form.instance.expert = self.request.user

        # filling the FollowUp model`s organization field with (continue in next line)
        # organization object with gotten pk in url querystring
        form.instance.organization = organmodels.Organization.objects.get(pk=self.kwargs['organization_pk'])
        form.save()

        return JsonResponse(data={
            'success': 'True',
            'success_message': _('Record Has Been Saved Successfully.')
        }, status=HTTP_201_CREATED)

    def form_invalid(self, form):
        return JsonResponse(data={
            'success': 'False',
            'error_message': _('Failed! Please Fill The Input Correctly.')
        }, status=HTTP_400_BAD_REQUEST)

    def get_context_data(self, **kwargs):
        context = {
            'organization_obj': organmodels.Organization.objects.get(pk=self.kwargs['organization_pk']),
        }
        return context
