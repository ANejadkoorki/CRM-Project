from django.urls import path
from . import views

# application name
app_name = 'sellProcess'

# urls:
urlpatterns = [
    path('add-quote/', views.AddQuote.as_view(), name='add-quote'),
    path('quote-list/', views.QuoteList.as_view(), name='quote-list'),
]
