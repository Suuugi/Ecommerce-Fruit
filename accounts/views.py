from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from accounts.forms import FullUserCreationForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class SignupCreateView(CreateView):
    form_class = FullUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')  

class UserLoginView(SuccessMessageMixin, LoginView):
    success_message = 'Successfully Logged In'

class UserLogoutView(LogoutView):
    next_page = 'index'