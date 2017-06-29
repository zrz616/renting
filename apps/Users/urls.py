from apps.Users.api import login_status, flush_captcha, create_account
from django.conf.urls import url, include
from apps.Users.views import UserLoginView, UserRegisterView
from rest_framework.authtoken import views

extra_urlpatterns = [
    url(r'^token-auth$', views.obtain_auth_token),
    url(r'^login_status$', login_status),
    url(r'^created_user$', create_account),
    url(r'^new_captcha$', flush_captcha),
]

urlpatterns = [
    url(r'^login/$', UserLoginView.as_view(), name='login'),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),

    url(r'^api/v1.0/', include(extra_urlpatterns))
]