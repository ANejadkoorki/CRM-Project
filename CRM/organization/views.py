from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from . import models, forms, serializers
from company import models as companyModels
from sellProcess import models as SPmodels
# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView


@method_decorator(csrf_exempt, name='dispatch')
class AddOrganization(LoginRequiredMixin, CreateView):
    """
        this view is used to create an Organization model object
    """
    model = models.Organization
    form_class = forms.OrganizationForm
    template_name = 'organization/add-organization-template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['ManufacturedProducts'] = models.OrganizationsProduct.objects.all()
        return context

    def form_valid(self, form):
        form.instance.expert = self.request.user
        form.save()
        messages.success(self.request, _('The Organization Has Been Saved Successfully.'))
        return redirect('organization:add-organization')

    def form_invalid(self, form):
        messages.error(self.request, _('Failed, Please Fill The Inputs Successfully.'))
        return redirect('organization:add-organization')


class OrganizationList(LoginRequiredMixin, ListView):
    """
        this view is used to list Organization model objects
    """
    model = models.Organization
    template_name = 'organization/list-organization.html'
    paginate_by = 4


@method_decorator(csrf_exempt, name='dispatch')
class EditOrganization(LoginRequiredMixin, UpdateView):
    """
        this view is used to update an Organization model object
    """
    model = models.Organization
    template_name = 'organization/edit_organization.html'
    extra_context = {'ManufacturedProducts': models.OrganizationsProduct.objects.all()}
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

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f"{self.request.POST.get('organization_name')}{_('Has Been Updated Successfully.')}")
        pk = self.get_object().pk
        return redirect('organization:organization-detail', pk)

    def form_invalid(self, form):
        messages.success(self.request, _(f"Failed.Please Fill The Inputs Carefully."))
        pk = self.get_object().pk
        return redirect('organization:edit-organization', pk)


@method_decorator(csrf_exempt, name='dispatch')
class AddOrganizationsProduct(LoginRequiredMixin, CreateView):
    """
        this view is used to create an OrganizationProduct model object
    """
    model = models.OrganizationsProduct
    template_name = 'organization/add-organizations-prod.html'
    fields = (
        'name',
    )

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f"{self.request.POST.get('name')}{_('Saved Successfully.')}")
        return redirect('organization:add-organizations-product')

    def form_invalid(self, form):
        messages.error(self.request, _('Failed! Please Enter the Product Name Carefully.'))
        return redirect('organization:add-organizations-product')


class OrganizationDetail(LoginRequiredMixin, DetailView):
    """
        this view is used to get an Organization model object details
    """
    model = models.Organization
    template_name = 'organization/organization-detail.html'

    # this method returns our company offers for each organization
    def get_offer_products(self):
        organization = self.get_object()  # organization object
        # organization object manufactured products
        org_manufactured_products = organization.manufactured_product.all()
        # offers : filtering in company product model objects
        offers = companyModels.CompanyProduct.objects. \
            filter(usable_for_organizations_product__in=org_manufactured_products).distinct()
        return offers

    # returning new context that have 'our_offer_products and follow up objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['our_offer_products'] = self.get_offer_products()
        context['organization_follow_up_objects'] = SPmodels.FollowUp.objects.filter(organization_id=self.kwargs['pk'])
        return context


"""
    DRF API VIEW SETS
"""


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(expert=self.request.user)
        return qs


class OrganizationsProductsViewSet(viewsets.ModelViewSet):
    queryset = models.OrganizationsProduct.objects.all()
    serializer_class = serializers.OrganizationsProductsSerializer
