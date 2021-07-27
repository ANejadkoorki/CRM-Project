from django.urls import path
from . import views

app_name = 'organization'

urlpatterns = [
    path('add-organization/', views.AddOrganization.as_view(), name='add-organization')
]
