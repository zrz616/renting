# from django import forms
# from django.contrib.auth import authenticate

# from formapi import calls
# from formapi.api import API
# from captcha.fields import CaptchaField


# class UserRegisterCall(calls.APICall):

#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput, min_length=7, max_length=20)
#     captcha = CaptchaField()

#     def __init__(self, *args, **kwargs):
#         self.user_cache = None
#         super(UserRegisterCall, self).__init__(*args, **kwargs)

#     def action(self):
#         pass
