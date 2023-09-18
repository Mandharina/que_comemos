from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    path('recetario/',views.recetario, name='recetario' ),
    path('login/<str:usuario>',views.login, name='login' ),
]