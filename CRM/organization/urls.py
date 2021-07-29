from django.urls import path
from . import views

app_name = 'organization'

urlpatterns = [
    path('add-organization/', views.AddOrganization.as_view(), name='add-organization'),
    path('add-organizations-product/', views.AddOrganizationsProduct.as_view(), name='add-organizations-product'),
    path('organization-list/', views.OrganizationList.as_view(), name='organization-list'),
    path('organization-detail/<int:pk>', views.OrganizationDetail.as_view(), name='organization-detail'),
    path('edit-organization/<int:pk>', views.EditOrganization.as_view(), name='edit-organization'),
]
