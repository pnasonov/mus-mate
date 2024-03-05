from django.contrib.auth.views import LoginView
from django.urls import path

from .views import logout_view, RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", logout_view, name="logout"),
]
