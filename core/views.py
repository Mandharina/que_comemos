from django.shortcuts import render
from django.http import HttpResponse

from . import forms

def index (request):
    return render(request, 'core/index.html')

def recetario (request):
    return render(request, "core/recetario.html")

'''
def login (request, usuario):
    return HttpResponse(f"Hola {usuario} ¿No sabés qué comer hoy?")
'''
def buscar(request):
    if request.method == "POST":
        ingrediente = request.POST.get("ingrediente")
        return render(request, 'core/recetario.html', {'ingrediente': ingrediente})
    else:
        return render(request, 'core/recetario.html', {'ingrediente': ' '})

def login(request):
    form = forms.LoginForm(request.POST)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
        
            contexto = {'form': form}
            return render(request, 'core/index.html', contexto)
        else:
            print('No Valido')
            return render(request, 'core/login.html', {'form': form})
    
    return render(request, 'core/login.html', {'form': form})
    

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        if form.is_valid():
            contexto = {'form': form}
            return render(request, 'core/index.html', contexto)
        else:
            return render(request, 'core/signup.html', {'form': form})
    return render(request, 'core/signup.html', {'form': form})