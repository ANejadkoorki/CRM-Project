from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . import models, forms
# Create your views here.
from django.views.generic import CreateView, ListView


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
