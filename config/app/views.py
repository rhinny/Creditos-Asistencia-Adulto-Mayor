from django.shortcuts import render, redirect
from .forms import *
from .models import *

def home(request):
    contexto = {'texto':"Home"}
    return render(request, "home.html",contexto)

def login_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_estudiante') #hasta ahora, redirige al index ,deberia dirigir a 'seleccion de apoyo'
    else:
        form = EstudianteForm()
    return render(request, 'login_estudiante.html',{'form':form})

def login_adultoM(request):
    if request.method == "POST":
        form = AdultoMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_adultoM') #hasta ahora, redirige al index ,deberia dirigir a 'seleccion de apoyo'
    else:
        form = AdultoMForm()
    return render(request, 'login_adultoM.html',{'form':form})
