from django.contrib import admin
from core.models import Receta, IngredienteMedido, Ingredientes, Organizador_Semanal, Usuario, MiRecetario

# Register your models here.

admin.site.register(Receta)
admin.site.register(IngredienteMedido)
admin.site.register(Ingredientes)
admin.site.register(Organizador_Semanal)
admin.site.register(Usuario)
admin.site.register(MiRecetario)
