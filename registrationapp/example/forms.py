from django.contrib.auth.models import User
from django import forms
import re


class signupForm(forms.Form):
    username = forms.CharField(
        label='Enter Your First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your First Name'
            }
        )
    )
    password = forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Password'
            }
        )
    )
    email = forms.CharField(
        label='Enter Your Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Make sure your password is at least 8 letters")
        if re.search('[0-9]', password) is None:
            raise forms.ValidationError("Make sure your password has min one digit in it")
        return password
