from django.urls import path
from django.contrib.auth.views import LoginView

from accounts.views import SignupCreateView, UserLoginView, UserLogoutView

# Provided URL Patterns for path('accounts/', include('django.contrib.auth.urls'))
# https://docs.djangoproject.com/en/4.1/topics/auth/default/#user-objects
urlpatterns = [
    path('signup/', SignupCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # Provided Out of the Box
    # ==============================
    # accounts/login/ [name='login'] - 1/21/2023
    # accounts/logout/ [name='logout'] - 1/25/2023
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
]
