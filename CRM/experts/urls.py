from django.urls import path
from . import views

app_name = 'experts'

# urls:
urlpatterns = [
    path('login/', views.ExpertLogin.as_view(), name='login'),
    path('logout/', views.ExpertLogout.as_view(), name='logout'),
    path('profile/<int:pk>', views.ExpertProfile.as_view(), name='profile'),
]
