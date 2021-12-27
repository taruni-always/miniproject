from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','password1', 'password2','email')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username']
