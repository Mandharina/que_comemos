from django.contrib import admin
from core.models import Receta, Ingredientes, MiRecetario

# Register your models here.

admin.site.register(Receta)

admin.site.register(Ingredientes)

admin.site.register(MiRecetario)
