from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('',views.index, name='index' ),
    #path('login/',views.login, name='login' ),
    #path('signup/',views.signup, name='signup' ),
    path('buscar/', views.buscar_recetas, name='buscar'),
    path('agregar_receta', views.AgregarRecetaCreateView.as_view(), name="agregar_receta"),
    path('editar_receta/<int:pk>', views.EditarRecetaUpdateView.as_view(), name ="editar_receta"),
    path('eliminar_receta/<int:pk>', views.EliminarRecetaDeleteView.as_view(), name ="eliminar_receta"),
    path('ver_receta/<int:pk>', views.VerRecetaDetailView.as_view(), name ="ver_receta"),
    path('recetario/',views.RecetarioListView.as_view(), name='recetario' ),
    path('agregar_a_recetario/<int:receta_id>/', views.agregar_a_recetario, name='agregar_a_recetario'),
    path('agregar_ingrediente', views.AgregarIngredienteCreateView.as_view(), name="agregar_ingrediente"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)