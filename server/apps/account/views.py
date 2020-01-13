from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from apps.account.models import User
from django.contrib import messages


class LoginView(View):
    def get(self, request, **kwargs):
        return render(request, 'registration/login.html')

    def post(self, request, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/login.html', {
                'error_msg': '이메일과 비밀번호를 확인해 주세요'
            })


class SignupView(View):
    def get(self, request, **kwargs):
        return render(request, 'registration/signup.html')

    def post(self, request, **kwargs):
        email = request.POST.get('email')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not name or not email or not password1:
            return redirect('/')

        if User.objects.filter(email=email).first():
            messages.warning(request, '이미 존재하는 계정입니다.')
            return redirect('/login/')

        if password1 != password2:
            return render(request, 'registration/signup.html', {
                'error_msg': '비밀번호가 일치하지 않습니다.'
            })

        user = User.objects.create_user(
            email=email, password=password1
        )
        user.username = name
        user.save()

        messages.success(request, '성공적으로 회원가입 되었습니다!')
        return redirect('/login/')
