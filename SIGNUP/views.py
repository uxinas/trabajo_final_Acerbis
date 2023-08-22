from django.http import HttpResponse
from django.shortcuts import render
from SIGNUP.models import Usuario_nuevo
from SIGNUP.forms import *
from LOGIN import views
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm 


def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"msj_usuario_creado.html" ,  {"mensaje":"Usuario creado con exito!"})
    
       # if request.user.is_authenticated:
           #return render(request,"inicio.html")
           

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})

def signup(request):
    return render(request,'signup.html')


def Usuario_nuevo_Formulario_vista(request):
    if request.method == "POST":
        miFormulario = Usuario_nuevo_Formulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario = Usuario_nuevo (nombre=informacion['nombre'], 
                            email=informacion['email'],
                            password=informacion['password'])
            usuario.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = Usuario_nuevo_Formulario()
        return render(request, 'signup.html', {'miFormulario':miFormulario})



    
