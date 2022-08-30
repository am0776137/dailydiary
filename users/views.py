from django.http import HttpResponse
from django.shortcuts import render, redirect
from users import forms
from users.forms import UserRegistrationForm
from django import forms

def register(request):
    if request.method=="POST":
        print("chal giya")
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("if k andr wala chal giya")
            form.save()
            username = form.cleaned_data.get('username')
            return redirect("diary-home")
        else:
            form = UserRegistrationForm()
            return render(request, "users/register.html", {'form':form})   

    else:
        form = UserRegistrationForm()
        return render(request, "users/register.html", {'form':form})


def profile(request):
    return render(request, "users/profile.html")
