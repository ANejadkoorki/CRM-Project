# Application Name
from django.urls import path
from . import views

app_name = 'emailApp'

urlpatterns = [
    path('send-email/<int:pk>', views.send_email_with_celery, name='send-email'),
]
