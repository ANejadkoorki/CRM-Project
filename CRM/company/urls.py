from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# application name
app_name = 'company'

# urls :
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('add-company-product/', views.AddCompanyProduct.as_view(), name='add-company-product'),
    path('list-company-product/', views.CompanyProductsList.as_view(), name='list-company-product'),
    path('company-product-detail/<int:pk>', views.CompanyProductDetail.as_view(), name='company-product-detail'),
    path('company-product-edit/<int:pk>', views.EditCompanyProduct.as_view(), name='company-product-edit'),
]

# passing STATIC URL and MEDIA URL to urls.py
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
