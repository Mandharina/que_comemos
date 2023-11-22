from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    
    path('login/',views.login, name='login' ),
    path('signup/',views.signup, name='signup' ),
    path('buscar/', views.buscar, name='buscar'),
    path('agregar_receta', views.AgregarRecetaCreateView.as_view(), name="agregar_receta"),
    path('editar_receta', views.EditarRecetaUpdateView.as_view(), name ="editar_receta"),
    path('recetario/',views.RecetarioListView.as_view(), name='recetario' ),
    #path('agregar_ingrediente', views.AgregarIngredienteCreateView.as_view(), name="agregar_ingrediente"),
]