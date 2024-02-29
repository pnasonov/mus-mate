from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import LoginForm, SignUpForm


def login_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("forum:home")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(
        request,
        "registration/login.html",
        {"form": form, "msg": msg},
    )


def register_view(request: HttpRequest) -> HttpResponse:
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect("forum:home")

        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(
        request,
        "registration/register.html",
        {"form": form, "msg": msg, "success": success},
    )


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)

    return redirect("login")
