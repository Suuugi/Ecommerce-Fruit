from django.urls import path

from django.views.generic import RedirectView
from store.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('github', RedirectView.as_view(url='https://github.com/Suuugi/Ecommerce-Fruit'), name='github')
]
