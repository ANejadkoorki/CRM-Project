from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView


class HomeView(View):
    """
        just returns Home Template
    """
    def get(self, request):
      return  render(request, 'company/home-template.html')


