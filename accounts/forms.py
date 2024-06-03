from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .models import User, Profile
from django.forms import ModelForm

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2', 'role']
        labels = {
            'first_name': 'Name'
        }


# User Profile form
class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['role']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email']