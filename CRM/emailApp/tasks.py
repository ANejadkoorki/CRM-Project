from celery import shared_task
from django.conf import settings
from django.contrib import messages

from . import models

from django.core.mail import send_mail, EmailMessage


@shared_task
def send_email_task(organization_name, quote_id, organization_representative_full_name,
                    organization_representative_email, sender_id):
    try:
        quote_email = EmailMessage(
            subject=f'Quote(ID:{quote_id}) for organization : {organization_name}',
            body=f'Hello Dear {organization_representative_full_name};'
                 f'\nThe Quote for your organization : {organization_name} has been recorded and'
                 f' posted in the attachment.',
            from_email=settings.EMAIL_HOST_USER,
            to=[
                organization_representative_email
            ],
            attachments=[

            ],
        )
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
