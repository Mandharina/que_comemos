from django.contrib import admin
from core.models import Ingredientes, Receta, MiRecetario
# Register your models here.
admin.site.register(Ingredientes)
admin.site.register(Receta)
admin.site.register(MiRecetario)

class IngredientesInline(admin.TabularInline):
    model = Receta.ingredientes.through

class IngredientesAdmin(admin.ModelAdmin):
    inlines=[
        IngredientesInline
    ]

class RecetaAdmin(admin.ModelAdmin):
    inlines = [
        IngredientesInline
    ]
    exclude=('ingredientes')