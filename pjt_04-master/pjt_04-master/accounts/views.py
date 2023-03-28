from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # 요청이 담긴 폼을 만들어서
        if form.is_valid():
            form.save()  # db에 반영
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()  # 빈 폼을 생성
    context = {'form':form}
    return render(request,'accounts/signup.html',context)

def delete(request):  # 회원탈퇴 뷰
    request.user.delete()  # user 데이터 삭제
    auth_logout(request)
    return render(request,'accounts/delete.html')  # 정상적으로 삭제되었음을 알려주기

def login(request):  # 로그인 뷰
    if request.method =='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request,'accounts/login.html',context)

def logout(request): 
    auth_logout(request)
    return render(request,'accounts/logout.html')