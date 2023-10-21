from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    path('recetario/',views.recetario, name='recetario' ),
    path('login/',views.login, name='login' ),
    path('signup/',views.signup, name='signup' ),
    path('buscar/', views.buscar, name='buscar'),
]