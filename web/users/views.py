from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from users.forms import LoginForm
from users.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect(request, "main_test.html")

    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

                return redirect(request, "main_test.html")

            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")

        context = {
            "form" : form
        }

    else:
        form = LoginForm()

        context = {
            "form" : form
        }

    return render(request, "users/login.html", context)