from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from . import models
from .tasks import send_email_task
from sellProcess import models as spmodels
from organization import models as organmodels


def send_email_with_celery(request, pk):
    """
        this email used to send email with celery task
    """
    # shaping Email requirements
    # sender
    sender_id = request.user.pk

    # quote
    quote_id = pk
    quote_object = spmodels.Quote.objects.get(pk=quote_id)
    quote_organization_id = quote_object.organization_id

    # organization
    organization = organmodels.Organization.objects.get(pk=quote_organization_id)
    organization_name = organization.organization_name
    organization_representative_email = organization.representative_email

    # quote html message
    html_message = render_to_string(
        template_name='sellProcess/quote-pdf.html',
        context={
            'object': quote_object,
        },
    )

    # function : send_email_task in below variable returns email history model object status
    email_result = send_email_task.delay(organization_name,
                                         quote_id,
                                         organization_representative_email,
                                         html_message,
                                         sender_id)

    # response message :
    if email_result:
        messages.success(request, 'Email Has Been Sent Successfully.')
    else:
        messages.error(request, 'Sending Email Failed.')

    return redirect('sellProcess:quote-list')
