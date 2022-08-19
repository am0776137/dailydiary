import re
from django.http import HttpResponse
from django.shortcuts import render, redirect

import users
from users.forms import UserRegistrationForm

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect("")
    else:
        form = UserRegistrationForm()
        return render(request, "users/register.html", {'form':form})


def profile(request):
    return render(request, "users/profile.html")