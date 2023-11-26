from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Receta, MiRecetario
from . import forms
from core.forms import RecetaForm, BusquedaIngredienteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index (request):
    return render(request, 'core/index.html')

@login_required
def recetario (request):
    return render(request, "core/recetario.html")

#-------------------------------------------------------------------------------------------

def buscar_recetas(request):
    if request.method == 'POST':
        form = BusquedaIngredienteForm(request.POST)
        if form.is_valid():
            ingrediente_nombre = form.cleaned_data['ingrediente']
            recetas = Receta.objects.filter(ingredientes__nombre__icontains=ingrediente_nombre)
            return render(request, 'core/resultados_busqueda.html', {'recetas': recetas, 'ingrediente': ingrediente_nombre})
    else:
        form = BusquedaIngredienteForm()

    return render(request, 'core/buscar.html', {'form': form})

def agregar_a_recetario(request, receta_id):
    receta = Receta.objects.get(id=receta_id)

    mi_recetario = MiRecetario(recetas=receta)
    mi_recetario.save()

    messages.info(request, "Receta agregada")
    return redirect('recetario')  # Puedes redirigir a otra página o hacer lo que sea necesario
    


#-------------------------------------------------------------------------------------------
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


#CRUD DE RECETAS

class AgregarRecetaCreateView(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'core/agregarreceta.html'
    success_url = 'recetario'
    #se sobreescribe el método
    def form_valid(self, form):
        response = super().form_valid(form)

        mi_recetario = MiRecetario(recetas=self.object)
        mi_recetario.save()

        return response


class EditarRecetaUpdateView(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'core/editarreceta.html'
    success_url = reverse_lazy ('recetario')


class EliminarRecetaDeleteView(DeleteView):
    model = Receta
    
    template_name = 'core/eliminarreceta.html'
    success_url = reverse_lazy('recetario')

#class RecetarioListView(ListView):
#    model = Receta
#    context_object_name = 'recetas'
#    template_name = 'core/recetario.html'
#    ordering = ['nombre']

class RecetarioListView(LoginRequiredMixin, ListView):
    model = MiRecetario
    template_name = 'core/recetario.html'
    context_object_name = 'mi_recetario_list'
    ordering = ['nombre']

    def get_queryset(self):
        return MiRecetario.objects.all()


