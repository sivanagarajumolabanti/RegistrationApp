from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .forms import signupForm

from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and  user.is_authenticated:
            auth_login(request, user)
            return render(request, "auth/success.html", context)
        else:
            context["error"] = "provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)


def logout(request):
    if request.method == "POST":
        return render(request, "auth/login.html")


def signup(request):
    form = signupForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')

        data = User(
            username=username,
            password=password,
            email=email
            )
        data.save()
        data.set_password(password)
        data.save()
        email = EmailMessage('Registration Notification', 'Thank you for registering to our site ', to=[data.email])

        email.send()
        return render(request, 'signup_success.html', context)
    else:
        return render(request, 'signup.html', context)


def change_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            username = request.POST['username']
            new_password = form.cleaned_data['new_password2']
            user = User._default_manager.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password has been reset.')
            login_url = '<a href="/login">Login </a>'
            return HttpResponse('Password has been reset. Login from here %s' % login_url)
        else:
            messages.error(request, 'Please correct the error below.')
            return HttpResponse(form.errors)
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'password_reset.html', {
        'form': form
    })
