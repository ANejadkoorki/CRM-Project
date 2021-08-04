from django.urls import path
from . import views

# application name
app_name = 'sellProcess'

# urls:
urlpatterns = [
    path('add-quote/', views.AddQuote.as_view(), name='add-quote'),
    path('quote-list/', views.QuoteList.as_view(), name='quote-list'),
    path('quote-detail/<int:pk>', views.QuoteDetail.as_view(), name='quote-detail'),
    path('quote-pdf/<int:pk>', views.QuotePdf.as_view(), name='quote-pdf'),
]
