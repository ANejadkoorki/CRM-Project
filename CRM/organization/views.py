from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . import models, forms
# Create your views here.
from django.views.generic import CreateView


@method_decorator(csrf_exempt, name='dispatch')
class AddOrganization(CreateView):
    model = models.Organization
    form_class = forms.OrganizationForm
    template_name = 'organization/add-organization-template.html'
    extra_context = {'ManufacturedProducts': models.OrganizationsProduct.objects.all()}

    def form_valid(self, form):
        form.instance.expert = self.request.user
        form.save()
        return JsonResponse(data={
            'success': 'True',
            'success_message': 'The Organization Has Been Saved Successfully.'
        }, status=201)

    def form_invalid(self, form):
        return JsonResponse(data={
            'success': 'False',
            'error_message': form.errors,
        }, status=400)
