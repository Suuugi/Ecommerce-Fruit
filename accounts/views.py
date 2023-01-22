from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from accounts.forms import FullUserCreationForm
from django.urls import reverse_lazy


class LoginTemplateView(LoginView):
    model = User
    # Default location with path('members/', include('django.contrib.auth.urls')),
    template_name = 'registration/login.html'
    next = 'index'


class SignupTemplateView(generic.CreateView):
    model = User
    form_class = FullUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

# TODO


def Profile(request):
    '''
    profile view
    '''
    return render(request, 'profile.html')
