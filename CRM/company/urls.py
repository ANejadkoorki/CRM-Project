from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('add-company-product/', views.AddCompanyProduct.as_view(), name='add-company-product'),
    path('list-company-product/', views.CompanyProductsList.as_view(), name='list-company-product'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
