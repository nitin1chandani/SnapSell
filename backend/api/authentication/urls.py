from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path("api/auth/register/", UserRegistrationView.as_view(), name="user-register"),
    path("api/auth/login/", UserLoginView.as_view(), name="user-login"),
    path("api/auth/logout/", UserLogoutView.as_view(), name="user-logout"),
]