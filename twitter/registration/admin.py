# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User

from django.contrib import admin
from registration.models import  Author
admin.register(User)

# Register your models here.

admin.site.register(Author)