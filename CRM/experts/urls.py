from django.urls import path
from . import views

app_name = 'experts'

urlpatterns = [
    path('login/',views.ExpertLogin.as_view(), name='login'),
    path('logout/', views.ExpertLogout.as_view(), name='logout'),
]
