from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages


def index(request):
    return render(request, "index.html", {
        'title': 'PatagónIA lab'
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password)#None
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'User or Password Mistake')


    return render(request, 'users/login.html', {

        })

def articles(request):
    return render(request, "articles.html", {

    })

def contacto(request):
    return render(request, "contacto.html", {

    })

def equipo(request):
    return render(request, "equipo.html", {

    })