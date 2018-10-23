from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationFrom(UserCreationForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2", "email",)