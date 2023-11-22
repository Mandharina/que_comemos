from django.db import models


class Ingredientes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.nombre


class Receta (models.Model):
    DIFICULTAD = (
        ('F', 'Fácil'),
        ('M', 'Media'),
        ('D', 'Difícil'),
    )

    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    dificultad = models.CharField(max_length=1, choices=DIFICULTAD)
    ingredientes = models.ManyToManyField(Ingredientes)
    descripcion = models.TextField()


    def recetacompleta(self):
        nombres_ingredientes = ', '.join(str(ingrediente) for ingrediente in self.ingredientes.all())
        return f"{self.nombre} {self.get_dificultad_display()} - Ingredientes: {nombres_ingredientes} - Descripción: {self.descripcion}"

    def __str__(self):
        return self.recetacompleta()


class MiRecetario(models.Model):
    recetas = models.ForeignKey(Receta, on_delete=models.CASCADE)

    def __str__(self):
        return  self.recetas.recetacompleta() #para una representación más detallada    

# class Organizador_Semanal (models.Model):
#         DIAS = (
#             ('LU', 'Lunes'),
#             ('MA', 'Martes'),
#             ('MI', 'Miércoles'),
#             ('JU', 'Jueves'),
#             ('VI', 'Viernes'),
#             ('SA', 'Sábado'),
#             ('DO', 'Domingo'),
#         )
#         PERIODO = (
#             ('AL', 'Almuerzo'),
#             ('CE', 'Cena')
#         )
#         recetas = models.ForeignKey(Receta, on_delete=models.CASCADE)
#         dias = models.CharField(max_length=2, choices=DIAS)
#         periodo = models.CharField(max_length=2, choices=PERIODO)

    #Using a FileField or an ImageField (see below) in a model takes a few steps:revisar documentación
    #foto = models.ImageField(upload_to='static/img'),
    
