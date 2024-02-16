from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from users.forms import LoginForm, SignupForm
from users.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def login_view(request):
    # 유저가 이미 로그인 되어 있을때의 기능
    if request.user.is_authenticated:
        # main_test가 아닌 진짜 페이지로 돌아가는 기능 만들때, render를 redirect로 바꾸기
        return redirect("/main/")

    # request 메서드가 POST일때 = 로그인 시도일 때의 기능
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        # form의 형태에 유효한 request를 받을 경우, 아이디 값과 비밀번호 값을 변수 할당
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            # 입력한 아이디/비밀번호 값이 db의 값과 일치하는 경우, 로그인 진행
            if user:
                login(request, user)
                # main_test가 아닌 진짜 페이지로 돌아가는 기능 만들때, render를 redirect로 바꾸기
                return redirect("/main/")

            # 입력한 아이디/비밀번호 값이 db의 값과 일치하지 않는 경우
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")

        context = {
            "form" : form
        }

    # 로그인 페이지에 접근하는 시도에 대한 처리
    else:
        form = LoginForm()

        context = {
            "form" : form
        }

    return render(request, "users/login.html", context)


def signup_view(request):

    # signup 시도에 대한 처리
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)

        # signup 시도가 승인되었을때, user 정보를 저장한
        if form.is_valid():
            user = form.save()
            # signup한 user를 로그인 시킨 후 main_test.html로 render
            login(request, user)
            # 현재는 임시로 render를 사용중이지만 추후 redirect로 변경해야함
            return redirect("/main/")
        
    # signup 페이지로 접속 시도 시의 처리
    else:
        form = SignupForm()

    context = {
        "form" : form
    }

    return render(request, "users/signup.html", context)

def logout_view(request):
    logout(request)
    return redirect("/main/")