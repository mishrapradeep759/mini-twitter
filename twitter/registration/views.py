# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.contrib.auth.forms import forms
from django.urls import reverse

from registration_form import UserRegistrationFrom
from signin_form import SignInForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Author


def registration_form(request):

    if request.method == "POST":
        registration_form = UserRegistrationFrom(request.POST)
        if registration_form.is_valid():
            print registration_form.cleaned_data # a dictionary with all fields we filled in a form
            # data = registration_form.cleaned_data
            # username = data["username"]
            # password = data["password"]
            username = registration_form.cleaned_data.get('username')
            registration_form.save()
            return redirect("/registration/account")

    else:
        registration_form = UserRegistrationFrom()

    return render(request, 'registration/register.html', {'form': registration_form})


def registered(request):
    user = User.objects.last()
    return HttpResponse("Welcome %s you have successfully registered!" % user)


def user(request, uid):
    user = User.objects.filter(pk=uid)
    return HttpResponse("Welcome %s you have successfully registered!" %user)

def signin_form(request):
    if request.method == "POST":
        signin_form = SignInForm(request.POST)
        if signin_form.is_valid():
            signin_form.save()
            return redirect("/user")

    else:
        signin_form = SignInForm()

    return render(request, 'registration/signin.html', {'form': signin_form})

def home(request):
    return redirect(reverse("registration:logout"))
