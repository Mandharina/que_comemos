from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse("Hola Manola")

def recetario (request):
    return HttpResponse("Ingresa tus ingredientes")

def login (request, usuario):
    return HttpResponse(f"Hola {usuario} ¿No sabés qué comer hoy?")