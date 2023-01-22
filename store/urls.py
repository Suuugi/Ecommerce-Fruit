from django.urls import path

from store import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]
