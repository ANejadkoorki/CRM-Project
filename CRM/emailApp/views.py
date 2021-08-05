from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from .tasks import send_email_task
from sellProcess import models as spmodels
from organization import models as organmodels


def send_email_with_celery(request, pk):
    # shaping Email requirements
    sender_id = request.user.pk
    quote_id = pk
    quote_organization_id = spmodels.Quote.objects.get(pk=pk).organization_id
    organization = organmodels.Organization.objects.get(pk=quote_organization_id)
    organization_name = organization.organization_name
    organization_representative_email = organization.representative_email
    organization_representative_full_name = organization.representative_full_name

    # send_email_task in below variable returns email history model object
    email_result = send_email_task.delay(organization_name, quote_id, organization_representative_full_name,
                                         organization_representative_email, sender_id)

    # response :
    if email_result:
        messages.success(request, 'Email Has Been Sent Successfully.')
    else:
        messages.error(request, 'Sending Email Failed.')

    return redirect('sellProcess:quote-list')
