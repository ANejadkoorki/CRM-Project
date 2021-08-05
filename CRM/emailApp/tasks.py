from celery import shared_task
from django.conf import settings
from django.contrib import messages

from . import models

from django.core.mail import send_mail, EmailMessage


@shared_task
def send_email_task(organization_name, quote_id, organization_representative_full_name,
                    organization_representative_email, html_message, sender_id):
    try:
        quote_email = EmailMessage(
            subject=f'Quote(ID:{quote_id}) for organization : {organization_name}',
            body=html_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[
                organization_representative_email
            ],
            attachments=[

            ],
        )
        quote_email.content_subtype = 'html'  # this is required because there is no plain text email message
        quote_email.send()
        email_history_object = models.EmailHistory.objects.create(
            receiver_email_address=organization_representative_email,
            is_successful=True,
            sender_id=sender_id,
        )
    except:
        email_history_object = models.EmailHistory.objects.create(
            receiver_email_address=organization_representative_email,
            is_successful=False,
            sender=sender_id,
        )

    return email_history_object.is_successful
