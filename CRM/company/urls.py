from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'company'


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
