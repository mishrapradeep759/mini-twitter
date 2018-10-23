from django.conf.urls import url, include
from django.contrib import admin
from . import views as user_view
from django.contrib.auth import views as auth_views
from registration.views import registered


app_name = "registration"

urlpatterns = [
    url(r'signup', user_view.registration_form, name='signup'),
    # url(r'login', user_view.signin_form, name='login'),
    url(r'account/', registered, name="accounts"),
    url(r'login/', auth_views.LoginView.as_view(template_name="registration/signin.html"), name='login'),
    url(r'logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    url(r'^(?P<uid>[0-9]+)/$', user_view.user, name="user"),
]