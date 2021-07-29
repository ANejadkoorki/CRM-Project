from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import models, forms
# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView


@method_decorator(csrf_exempt, name='dispatch')
class AddOrganization(LoginRequiredMixin, CreateView):
    model = models.Organization
    form_class = forms.OrganizationForm
    template_name = 'organization/add-organization-template.html'
    extra_context = {'ManufacturedProducts': models.OrganizationsProduct.objects.all()}

    def form_valid(self, form):
        form.instance.expert = self.request.user
        form.save()
        messages.success(self.request, 'The Organization Has Been Saved Successfully.')
        return redirect('organization:add-organization')

    def form_invalid(self, form):
        messages.error(self.request, 'Failed, Please Fill The Inputs Successfully.')
        return redirect('organization:add-organization')


class OrganizationList(LoginRequiredMixin, ListView):
    model = models.Organization
    template_name = 'organization/list-organization.html'
    paginate_by = 4


@method_decorator(csrf_exempt, name='dispatch')
class EditOrganization(LoginRequiredMixin, UpdateView):
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
        messages.success(self.request, f"{self.request.POST.get('organization_name')} Has Been Updated Successfully.")
        pk = self.get_object().pk
        return redirect('organization:organization-detail', pk)

    def form_invalid(self, form):
        messages.success(self.request, f"Failed.Please Fill The Inputs Carefully.")
        pk = self.get_object().pk
        return redirect('organization:edit-organization', pk)


@method_decorator(csrf_exempt, name='dispatch')
class AddOrganizationsProduct(LoginRequiredMixin, CreateView):
    model = models.OrganizationsProduct
    template_name = 'organization/add-organizations-prod.html'
    fields = (
        'name',
    )

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f"{self.request.POST.get('name')} Saved Successfully.")
        return redirect('organization:add-organizations-product')

    def form_invalid(self, form):
        messages.error(self.request, 'Failed! Please Enter the Product Name Carefully.')
        return redirect('organization:add-organizations-product')


class OrganizationDetail(LoginRequiredMixin, DetailView):
    model = models.Organization
    template_name = 'organization/organization-detail.html'

    def get_offer_products(self):
        organization = self.get_object()
        offers = set()
        for organization_product in organization.manufactured_product.all():
            for company_product in organization_product.companyproduct_set.all():
                offers.add(company_product)
        return offers

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['our_offer_products'] = self.get_offer_products()
        return context
