from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

'''
def index(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, "signup.html")


@csrf_exempt
def login(request):
    if request.method == 'POST' :
        print("리퀘스트 로그"+ str(request.body))
        id = request.POST.get('userName','')
        pw = request.POST.get('userPassword','')
        print(id, pw)


        # DB 연결 후 검증하는 부분

        if id and pw:  # 연결 성공 시
            return redirect('/search/')
        else:  # 실패시
            messages.warning(request, "권한이 없습니다.")
            return redirect('/')  # 홈페이지로 리디렉션

            # POST 요청이 아닌 경우 (GET 요청 등), 로그인 페이지를 표시
    return render(request, 'login.html')

'''