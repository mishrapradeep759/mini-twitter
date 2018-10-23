# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return 'abc'