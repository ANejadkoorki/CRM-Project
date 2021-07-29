from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from . import models
from organization import models as organ_models
from django.views.generic import ListView, CreateView, DetailView


class HomeView(View):
    """
        just returns Home Template
    """

    def get(self, request):
        return render(request, 'company/home-template.html')


@method_decorator(csrf_exempt, name='dispatch')
class AddCompanyProduct(LoginRequiredMixin, CreateView):
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
        messages.success(self.request, f"{self.request.POST.get('product_name')} Has Been Saved Successfully.")
        return redirect('company:add-company-product')

    def form_invalid(self, form):
        messages.error(self.request, "Failed. Please Fill The Inputs Correctly.")
        return redirect('company:add-company-product')


class CompanyProductsList(LoginRequiredMixin, ListView):
    model = models.CompanyProduct
    template_name = 'company/list-company-prod-.html'
    paginate_by = 3


class CompanyProductDetail(LoginRequiredMixin, DetailView):
    model = models.CompanyProduct
    template_name = 'company/company-product-detail.html'
