from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.core.mail import EmailMessage
from django.shortcuts import render


def RegistrationformView(request):
    form = RegistrationForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        data = User(
            username=first_name+last_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            )
        data.save()
        email = EmailMessage('Registration Notification', 'Thank you for registering to our site ', to=[data.email])
        email.send()
        return render(request, 'signup form.html', context)
    else:
        return render(request, 'signup form.html', context)


def UserList(request):
    users = User.objects.all()
    return render(request, "userlist.html", {'users': users})
