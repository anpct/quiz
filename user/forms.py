from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from user.models import Resp
 
 
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=10, max_length=10)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    firstname = forms.CharField(label='Enter name', min_length=1, max_length=60)
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_firstname(self):
        firstname = self.cleaned_data.get('firstname')

        return firstname
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'], 
            first_name= self.cleaned_data['firstname'],
            password= self.cleaned_data['password1']
        )
        return user


class PkForm(forms.ModelForm):
    class Meta:
        model = Resp
        fields = ['passkey']