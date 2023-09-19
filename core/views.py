from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request, 'core/index.html')

def recetario (request):
    return render(request, "core/recetario.html")

def login (request, usuario):
    return HttpResponse(f"Hola {usuario} ¿No sabés qué comer hoy?")