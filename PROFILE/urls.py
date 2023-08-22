from django.urls import path
from PROFILE import views



urlpatterns = [
    
    path('perfiles', views.profile, name='perfiles'),
    path('editarPERFIL', views.editarPerfil, name='Editarperfil'),
    path('editarusuarios_int/<first_name>', views.editarUsuarios_int, name='Editarusuarios_int'),
    path('leer_usuarios_int', views.leerUsuarios_int, name='leer_usuarios_int'),
    path('eliminarUsuarios_int/<first_name>', views.eliminarUsuarios_int, name='EliminarUsuarios_int'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),

    ]

