from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from accounts.models import User, Profile
from django.forms import ModelForm

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2', 'role']
        labels = {
            'first_name': 'Name'
        }
    # add class to the input field
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input form-control'})


# User Profile form
class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

# add class to the input field
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input form-control'})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['role']

# add class to the input field
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input form-control'})

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email']

# add class to the input field
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input form-control'})