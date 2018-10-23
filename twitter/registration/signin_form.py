from django.contrib.auth.forms import forms

class SignInForm(forms.Form):

    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
