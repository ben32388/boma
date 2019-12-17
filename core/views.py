from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        #註冊完直接登入
        login(request,user)
        return redirect('index')
    return render(request,'registration/register.html',{
        'form' : form,
    })

def index(request):
    return render(request,'registration/index.html')