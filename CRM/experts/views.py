from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import FormView, RedirectView, DetailView, UpdateView

from . import forms

# Create your views here.
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ExpertLogin(FormView):
    """
        this view used for authenticating and logging in an expert
    """
    form_class = forms.LoginForm
    template_name = 'experts/login-template.html'

    def form_valid(self, form):
        username, password = form.cleaned_data['username'], form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            next_url = self.request.GET.get('next', '/')
            if is_safe_url(next_url, settings.ALLOWED_HOSTS):
                messages.success(self.request, f'{self.request.user.username} Have Been Logged in Successfully.')
                return redirect(next_url)
            else:
                messages.error(self.request, 'This url is not safe.')
                return redirect('/')
        else:
            messages.error(self.request, 'The User Not Found.')
            return redirect('experts:login')

    def form_invalid(self, form):
        messages.error(self.request, 'Please Enter your Information Correctly.')
        return redirect('experts:login')


class ExpertLogout(RedirectView):
    """
        this view used for logging out an expert
    """

    def get(self, request, *args, **kwargs):
        messages.success(self.request, f'{self.request.user.username} Have Been Logged out Successfully.')
        logout(self.request)
        return redirect('company:home')


class ExpertProfile(LoginRequiredMixin, DetailView):
    """
        this view used to get  a User model object details
    """
    model = get_user_model()
    template_name = 'experts/profile.html'


@method_decorator(csrf_exempt, name='dispatch')
class ProfileEdit(LoginRequiredMixin, UpdateView):
    """
        this view used to update a User model Object
    """
    model = get_user_model()
    template_name = 'experts/edit-profile.html'
    fields = (
        'first_name',
        'last_name',
        'username',
    )

    # form validation
    def form_valid(self, form):
        user = self.get_object()
        form.save()
        messages.success(self.request, f'User : {user.username} Details Updated Successfully.')
        return redirect('experts:profile', user.pk)

    def form_invalid(self, form):
        messages.error(self.request, 'Please Fill The Inputs Correctly.')
        user_pk = self.get_object().pk
        return redirect('experts:edit-profile', user_pk)



