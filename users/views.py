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

        if id is not None:

            # print("인증성공")
            # login(request, user)  # 고칠 것
            return redirect('/search/') # 고칠 것
        else:
            print("인증실패")

            # 시간되면 로그인 실패 페이지랑
            # return render(request, "users/login.html")
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

        '''
        # db에 회원 정보 저장
        sql = f"insert into users(id, pw, birthday, gender) values ('{id}', '{pw}', '{birthday}', '{gender}')"
        c.execute(sql)  # sql 변수에 담긴 구문 실행
        conn.commit()   # db에 적용
        conn.close()    # db 접속 해제
        '''
        return redirect("user:login")

    return render(request, "users/signup.html")