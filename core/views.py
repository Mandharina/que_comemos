from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Receta, MiRecetario
from . import forms
from core.forms import RecetaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index (request):
    return render(request, 'core/index.html')

@login_required
def recetario (request):
    return render(request, "core/recetario.html")

'''
def login (request, usuario):
    return HttpResponse(f"Hola {usuario} ¿No sabés qué comer hoy?")
'''

@login_required
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

class AgregarRecetaCreateView(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'core/agregarreceta.html'
    success_url = 'recetario'


class EditarRecetaUpdateView(LoginRequiredMixin, UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name_suffix = 'core/editarreceta.html'
    
    

class RecetarioListView(ListView):
    model = MiRecetario
    context_object_name = 'recetario'
    template_name = 'core/recetario.html'

