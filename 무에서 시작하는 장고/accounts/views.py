from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm(request)

    context = {'form':form}
    return render(request,'accounts/login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 객체 생성해서 저장해서 유저에 담기
            auth_login(request,user)  # 해당 유저를 로그인 시켜 그리고
            return redirect('articles:index')  # 목록으로 돌아가
    else:
        form = CustomUserCreationForm()  # 빈폼을 만들어서
    context = {'form':form}
    return render(request,'accounts/signup.html',context)  # 그려줘

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()  # 객체 생성해서 저장해서 유저에 담기
            return redirect('articles:index')  # 목록으로 돌아가'
    else:
        form = CustomUserChangeForm(instance=request.user)  # 빈폼을 만들어서
    context = {'form':form}
    return render(request,'accounts/update.html',context)  # 그려줘

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()  # 객체 생성한 걸 반영해주고
            update_session_auth_hash(request,form.user)  # 비번 변경된 걸 변경해서
            return redirect('articles:index')  # 목록으로 돌아가'
    else:
        form = PasswordChangeForm(request.user)  # 빈폼을 만들어서
    context = {'form':form}
    return render(request,'accounts/change_password.html',context)  # 그려줘