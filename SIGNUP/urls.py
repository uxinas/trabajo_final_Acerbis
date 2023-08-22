from django.urls import path
from SIGNUP import views
from MAIN import urls
#from LOGIN import urls, views




urlpatterns = [
    
    #path('signup', views.signup, name='signup'),
    path('usuario_nuevo_formulario', views.Usuario_nuevo_Formulario_vista, name='usuario_nuevo'),
    path('register', views.register, name='Register'),

    ]