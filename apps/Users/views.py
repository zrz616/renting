from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm


class UserLoginView(View):
    """docstring for UserLoginView"""
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
        return render(request, 'login.html', {})


class UserRegisterView(View):
    """docstring for UserRegister"""
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
