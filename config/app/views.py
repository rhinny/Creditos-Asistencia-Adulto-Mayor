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
            form.save
            return redirect('agregar_libro') #deberia dirigir a la pestaña de elegir en lo que quiere ayudar, que es otro form
    else:
        form = EstudianteForm()
    return render(request, 'login_estudiante.html',{'form':form})

'''  
def login_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('app') #deberia dirigir a la pestaña de elegir en lo que quiere ayudar, que es otro form
        else:
            form = EstudianteForm()
        return render(request, 'login_estudiante.html',{'form':form})


def login_adultoM(request):
    if request.method == "POST":
        form = AdultoForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('app') #deberia dirigir a la pestaña de elegir en lo que quiere ayudar, que es otro form
        else:
            form = AdultoForm()
        return render(request, 'login_adultoM.html',{'form':form})
'''  