from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from . import models
from organization import models as organ_models
from django.views.generic import ListView, CreateView, DetailView, UpdateView


class HomeView(View):
    """
        just returns Home Template
    """

    def get(self, request):
        return render(request, 'company/home-template.html')


@method_decorator(csrf_exempt, name='dispatch')
class AddCompanyProduct(LoginRequiredMixin, CreateView):
    """
        this view used to create an CompanyProduct model object
    """
    model = models.CompanyProduct
    template_name = 'company/add-company-product-template.html'
    extra_context = {'OrganizationsProducts': organ_models.OrganizationsProduct.objects.all()}
    fields = (
        'product_name',
        'price',
        'have_tax',
        'pdf_catalog',
        'image_catalog',
        'technical_desc',
        'usable_for_organizations_product',
    )

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f"{self.request.POST.get('product_name')}{_('Has Been Saved Successfully.')}")
        return redirect('company:add-company-product')

    def form_invalid(self, form):
        messages.error(self.request, _("Failed. Please Fill The Inputs Correctly."))
        return redirect('company:add-company-product')


class CompanyProductsList(LoginRequiredMixin, ListView):
    """
        this view used to List CompanyProduct model objects
    """
    model = models.CompanyProduct
    template_name = 'company/list-company-prod-.html'
    paginate_by = 3


class CompanyProductDetail(LoginRequiredMixin, DetailView):
    """
        this view used to get an CompanyProduct model object details
    """
    model = models.CompanyProduct
    template_name = 'company/company-product-detail.html'


@method_decorator(csrf_exempt, name='dispatch')
class EditCompanyProduct(LoginRequiredMixin, UpdateView):
    """
        this view used to update an CompanyProduct model object
    """
    model = models.CompanyProduct
    template_name = 'company/edit-company-prod.html'
    extra_context = {'OrganizationProducts': organ_models.OrganizationsProduct.objects.all()}
    fields = (
        'product_name',
        'price',
        'have_tax',
        'pdf_catalog',
        'image_catalog',
        'technical_desc',
        'usable_for_organizations_product',
    )

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f"{self.request.POST.get('product_name')}{_('Has Been Updated Successfully.')}")
        pk = self.get_object().pk
        return redirect('company:company-product-detail', pk)

    def form_invalid(self, form):
        messages.error(self.request, _(f"Failed.Please Fill The Inputs Carefully."))
        pk = self.get_object().pk
        return redirect('company:company-product-edit', pk)
