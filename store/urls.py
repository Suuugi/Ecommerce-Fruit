from django.urls import path

from django.views.generic import RedirectView
from store.views import HomepageListView
from store.views import add_to_cart
from store.models import Order, OrderItem, Product

urlpatterns = [
    path('', HomepageListView.as_view(), name='home'),
    path('facebook', RedirectView.as_view(url='https://www.facebook.com/nick.sugimoto'), name='facebook'),
    path('github', RedirectView.as_view(url='https://github.com/Suuugi'), name='github'),
    path('linkedin', RedirectView.as_view(url='https://www.linkedin.com/in/nicholassugimoto'), name='linkedin'),
    path('add-to-cart/<int:product_id>', add_to_cart, name='add-to-cart')
]
