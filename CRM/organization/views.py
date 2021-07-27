from django.shortcuts import render
from . import models, forms
# Create your views here.
from django.views.generic import CreateView


class AddOrganization(CreateView):
    model = models.Organization
    form_class = forms.OrganizationForm
    template_name = 'organization/add-organization-template.html'
    extra_context = {'ManufacturedProducts': models.OrganizationsProduct.objects.all()}

    def form_valid(self, form):
        form.instance.expert = self.request.user

    def form_invalid(self, form):
        pass
