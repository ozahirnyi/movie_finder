from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=2, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput,
                                min_length=4)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput, min_length=4)
