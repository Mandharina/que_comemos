from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm    
from django.core.exceptions import ValidationError
from .models import Receta, Ingredientes

class BusquedaIngredienteForm(forms.Form):
    ingrediente = forms.CharField(max_length=100, label='Ingrediente')

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', required=True)
    email = forms.EmailField(label='Email', required=True)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if email not in ('oteronicolas3@gmail.com', 
                        'veronicahassen@gmail.com', 
                        'schiavone.marcelo@gmail.com', 
                        'alessandro.brizuela06@gmail.com', 
                        'mar@gmail.com'):
            raise ValidationError('El email no está en la base de datos!')
        
        return email

class SignupForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', required=True)
    email = forms.EmailField(label='Email', required=True)
    contrasena1 = forms.CharField(label='Contrasena', required=True)
    contrasena2 = forms.CharField(label='Repita Contrasena', required=True)


class RecetaForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    dificultad = forms.ChoiceField(
        label="Dificultad",
        choices=Receta.DIFICULTAD,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    ingredientes = forms.ModelMultipleChoiceField(
        label='Ingredientes',
        queryset=Ingredientes.objects.all(),
        widget=FilteredSelectMultiple("Ingredientes", is_stacked=False),
    
    )
    
    descripcion = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control', 'placeholder': 'Detallá los pasos'})
    )

    
    class Meta:
        model = Receta
        fields = ("nombre", "dificultad", "ingredientes", "descripcion" ,"imagen",)

class IngredienteForm(ModelForm):
    class Meta:
        model = Ingredientes
        fields = '__all__'
