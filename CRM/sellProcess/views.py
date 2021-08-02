from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class AddQuote(LoginRequiredMixin, CreateView):
    model = models.Quote
    template_name = 'sellProcess/add-quote.html'
