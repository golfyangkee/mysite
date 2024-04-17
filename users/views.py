from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout
from .models import User

def index(request):
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        id = request.POST.get('userName', '')
        pw = request.POST.get('userPassword', '')

        # 유저 네임과 패스워드가 존재하면 유저 객체 만들고 아니면 None으로 준다.
        user = authenticate(username=id, password=pw)  # 고칠 것

        if user is not None:

            # print("인증성공")
            login(request, user)  # 고칠 것
            return redirect('/search/') # 고칠 것
        else:
            print("인증실패")

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        id= request.POST["userName"]
        pw = request.POST["userPassword"]
        pw_check = request.POST["userPasswordCheck"]
        birthday = request.POST["userBirthday"]
        gender = request.POST["gender"]

        # 회원 정보 저장
        user = User.objects.create_user(username=id, password=pw)
        user.birthday = birthday
        user.gender = gender
        user.save()

        return redirect("user:login")

    return render(request, "users/signup.html")