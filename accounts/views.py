from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout, get_user_model
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import SignUpForm


class RegisterView(generic.CreateView):
    model = get_user_model()
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)

    return redirect("login")
