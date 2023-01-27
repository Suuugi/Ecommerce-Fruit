from django.urls import path

from django.views.generic import RedirectView
from store.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('github', RedirectView.as_view(url='https://github.com/Suuugi/Ecommerce-Fruit'), name='github'),
    path('linkedin', RedirectView.as_view(url='https://www.linkedin.com/in/nicholassugimoto'), name='linkedin')
]
