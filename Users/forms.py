from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=7, max_length=20)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=7, max_length=20)
    confirmed_password = forms.CharField(required=True, min_length=7, max_length=20)
    captcha = CaptchaField()
