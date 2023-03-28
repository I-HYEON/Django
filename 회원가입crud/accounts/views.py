from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm,CustomUserChangeForm
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
            user = form.save()  # user 객체 생성해주고
            auth_login(request,user)  # 해당 user 로그인 시켜주기
            return redirect('articles:index')  # 그리고 index화면으로 보내깃
    else:
        form = CustomUserCreationForm()  # 빈 폼 형성
    context = {'form':form}
    return render(request,'accounts/signup.html',context)


def delete(request):
    request.user.delete()  # user를 데려와서 삭제시키고
    auth_logout(request)  # 로그아웃시키기
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()  # 객체 생성해주고
            return redirect('articles:index')  # 그리고 index화면으로 보내깃
    else:
        form = CustomUserChangeForm(instance=request.user)  # 빈 폼 형성
    context = {'form':form}
    return render(request,'accounts/update.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()  # 객체 생성한거 반영해주고
            update_session_auth_hash(request,form.user)
            return redirect('articles:index')  # 그리고 index화면으로 보내깃
    else:
        form = PasswordChangeForm(request.user)  # 빈 폼 형성
    context = {'form':form}
    return render(request,'accounts/change_password.html',context)