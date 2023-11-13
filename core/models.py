from django.db import models

class Usuario(models.Model):
    pass


class MiRecetario(models.Model):
    pass


class Ingredientes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.nombre


class IngredienteMedido(Ingredientes):

    UNIDAD_DE_MEDIDA = (
        ('GR', 'Gramos'),
        ('KG', 'Kilogramos'),
        ('Cu', 'Cucharada'),
        ('CS', 'Cucharada sopera'),
        ('CC', 'Cucharadita de postre'),
        ('VA', 'Vaso'),
        ('ML', 'Mililitro'),
        ('UN', 'Unidad'),
   )
    unidad_de_medida = models.CharField(max_length=2, choices=UNIDAD_DE_MEDIDA)
    cantidad = models.IntegerField(verbose_name="cantidad")

    def detalleingrediente(self):
        return f"{self.nombre} {self.cantidad} {self.unidad_de_medida}" 

    def __str__(self):
        return self.detalleingrediente()


class Receta (models.Model):
    DIFICULTAD = (
        ('F', 'Fácil'),
        ('M', 'Media'),
        ('D', 'Difícil'),
    )

    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    dificultad = models.CharField(max_length=1, choices=DIFICULTAD)
    ingredientes = models.ManyToManyField(IngredienteMedido)
    descripcion = models.TextField()


    def recetacompleta(self):
        return f"{self.nombre} {self.dificultad} {self.detalleingrediente()} {self.descripcion}"

    def __str__(self):
        return self.recetacompleta()


class Organizador_Semanal (models.Model):
        DIAS = (
            ('LU', 'Lunes'),
            ('MA', 'Martes'),
            ('MI', 'Miércoles'),
            ('JU', 'Jueves'),
            ('VI', 'Viernes'),
            ('SA', 'Sábado'),
            ('DO', 'Domingo'),
        )
        PERIODO = (
            ('AL', 'Almuerzo'),
            ('CE', 'Cena')
        )
        recetas = models.ForeignKey(Receta, on_delete=models.CASCADE)
        dias = models.CharField(max_length=2, choices=DIAS)
        periodo = models.CharField(max_length=2, choices=PERIODO)





    #Using a FileField or an ImageField (see below) in a model takes a few steps:revisar documentación
    #foto = models.ImageField(upload_to='static/img'),
    
