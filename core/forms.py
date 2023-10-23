from django import forms
from django.forms import ModelForm    
from django.core.exceptions import ValidationError
from .models import Receta, IngredienteMedido

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


class AltaRecetaForm(ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

class AgregarIngredienteForm(ModelForm):
    class Meta:
        model = IngredienteMedido
        fields = '__all__'

