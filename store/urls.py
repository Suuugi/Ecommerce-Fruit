from django.urls import path

from store import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index')
]
