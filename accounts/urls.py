from django.urls import path

from accounts import views

# Provided URL Patterns for path('accounts/', include('django.contrib.auth.urls'))
# https://docs.djangoproject.com/en/4.1/topics/auth/default/#user-objects
urlpatterns = [
    path('signup/', views.SignupTemplateView.as_view(), name='signup'),
    path('profile/', views.Profile, name='profile') # We need to create our own view for profile
    # Provided Out of the Box
    # ==============================
    # accounts/login/ [name='login'] - 1/21/2023
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
]
