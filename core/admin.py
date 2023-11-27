from django.contrib import admin
from core.models import Ingredientes, Receta, MiRecetario


class IngredientesAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    #list_editable = ['nombre']

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dificultad', 'descripcion')
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'ingredientes':
            kwargs["queryset"] = Ingredientes.objects.filter().order_by("nombre")

        return super().formfield_for_manytomany(db_field, request, **kwargs)
    
# Register your models here.
admin.site.register(Ingredientes, IngredientesAdmin)
#admin.site.register(Receta)
admin.site.register(MiRecetario)