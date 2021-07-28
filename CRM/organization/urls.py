from django.urls import path
from . import views

app_name = 'organization'

urlpatterns = [
    path('add-organization/', views.AddOrganization.as_view(), name='add-organization'),
    path('organization-list/', views.OrganizationList.as_view(), name='organization-list'),
    path('organization-detail/<int:pk>', views.OrganizationDetail.as_view(), name='organization-detail'),
]
