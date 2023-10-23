from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    path('recetario/',views.recetario, name='recetario' ),
    path('login/',views.login, name='login' ),
    path('signup/',views.signup, name='signup' ),
    path('buscar/', views.buscar, name='buscar'),
    path('agregar_receta', views.AgregarRecetaNombreCreateView.as_view(), name="agregar_receta"),
    path('agregar_ingrediente', views.AgregarIngredienteCreateView.as_view(), name="agregar_ingrediente"),
]