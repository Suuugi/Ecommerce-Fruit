from django.urls import path

from django.views.generic import RedirectView
from store.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('facebook', RedirectView.as_view(url='https://www.facebook.com/nick.sugimoto'), name='facebook'),
    path('github', RedirectView.as_view(url='https://github.com/Suuugi'), name='github'),
    path('linkedin', RedirectView.as_view(url='https://www.linkedin.com/in/nicholassugimoto'), name='linkedin'),
]
