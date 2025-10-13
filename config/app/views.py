from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm

def home(request):
    contexto = {'texto':"Home"}
    return render(request, "home.html",contexto)

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "usuarios/registro.html", {'form':form})

'''
def registro_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_estudiante') #hasta ahora, redirige al index ,deberia dirigir a 'seleccion de apoyo'
    else:
        form = EstudianteForm()
    return render(request, 'registro_estudiante.html',{'form':form})

def registro_adultoM(request):
    if request.method == "POST":
        form = AdultoMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_adultoM') #hasta ahora, redirige al index ,deberia dirigir a 'seleccion de apoyo'
    else:
        form = AdultoMForm()
    return render(request, 'registro_adultoM.html',{'form':form})
'''