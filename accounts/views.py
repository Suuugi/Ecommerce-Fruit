from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from accounts.forms import FullUserCreationForm
from django.urls import reverse_lazy


class SignupCreateView(CreateView):
    form_class = FullUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserLogoutView(LogoutView):
    next_page = 'index'