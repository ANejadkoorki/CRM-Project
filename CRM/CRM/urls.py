"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from company import views as company_views
from experts import views as expert_views
from organization import views as organ_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

# api router

router = DefaultRouter()
router.register('experts', expert_views.ExpertViewSet)
router.register('organ/api/organizations', organ_views.OrganizationViewSet)
router.register('organ/api/organizationsProducts', organ_views.OrganizationsProductsViewSet)

# urls:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', company_views.HomeView.as_view()),
    path('company/', include('company.urls')),
    path('experts/', include('experts.urls')),
    path('organization/', include('organization.urls')),
    path('sellProcess/', include('sellProcess.urls')),
    path('email/', include('emailApp.urls')),
    path('api/v1/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# passing STATIC URL and MEDIA URL to project`s root
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
