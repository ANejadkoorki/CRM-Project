from django.http import HttpResponse
from django.shortcuts import render, redirect

from .tasks import send_email_task
from sellProcess import models as spmodels
from organization import models as organmodels


def send_email_with_celery(request, pk):
    sender = request.user
    quote_id = pk
    quote_organization_id = spmodels.Quote.objects.get(pk=pk).organization_id
    organization = organmodels.Organization.objects.get(pk=quote_organization_id)
    organization_name = organization.organization_name
    organization_representative_email = organization.representative_email
    organization_representative_full_name = organization.representative_full_name
    send_email_task.delay(request, organization_name, quote_id, organization_representative_full_name,
                          organization_representative_email, sender)
    return redirect('sellProcess:quote-list')
