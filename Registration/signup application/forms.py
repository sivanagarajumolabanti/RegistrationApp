from django.contrib.auth.models import User
from django import forms
import re


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='Enter Your First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your First Name'
            }
        )
    )
    last_name = forms.CharField(
        label='Enter Your Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Last Name'
            }
        )
    )

    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError('This email address is already registered.')
        if not re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            raise forms.ValidationError('This is not a valid email address')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Make sure your password is at least 8 letters")
        if re.search('[0-9]', password) is None:
            raise forms.ValidationError("Make sure your password has min one digit in it")
        if re.search('[A-Z]', password) is None:
            raise forms.ValidationError("Make sure your password has a min one capital letter in it")
        return password
