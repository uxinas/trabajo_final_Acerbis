from django.shortcuts import render
from SIGNUP.models import Usuario_nuevo
from PROFILE.forms import UserRegisterForm, UserEditForm, AvatarFormulario
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from LOGIN import views
from django.contrib import admin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Avatar
from SIGNUP.forms import Usuario_nuevo_Formulario


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request, "inicio.html" ,{'url':avatares[0].imagen.url})
    else:
        miFormulario=AvatarFormulario()
        
    return render(request, "agregarAvatar.html", {'miFormulario': miFormulario})



def profile(request):
    return render(request,'profile.html')


#@login_required

@permission_required('PROFILE.can_view_data')
def leerUsuarios_int(request):
    users = User.objects.all()
    contexto = {'Users':users}
    return render(request, 'leer_usuarios_int.html', contexto)



def eliminarUsuarios_int(request,first_name):
    usuario = User.objects.get(id=first_name)
    usuario.delete()

    usuarios = User.objects.all()
    contexto = {'Users':usuarios}

    return render(request, 'leer_usuarios_int.html', contexto )




def editarUsuarios_int(request, first_name):
    user = User.objects.get(username=first_name)
    
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
    

        if miFormulario.is_valid:
            informacion = miFormulario

            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.last_name = informacion['last_name']
            user.first_name = informacion['first_name']


            user.save()

            return render(request, 'editarUsuarios.html')
    else:
        miFormulario = UserEditForm(initial={'email': user.email})

    return render(request, 'editarUsuarios.html', {'miFormulario':miFormulario, 'user': user}) 

"""
def editarUsuarios_int(request, first_name):
    user = User.objects.get(username=first_name)
    
    if request.method == "POST":
        miFormulario = Usuario_nuevo_Formulario (request.POST)
        print(miFormulario)
    

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.last_name = informacion['last_name']
            user.first_name = informacion['first_name']


            user.save()

            return render(request, 'editusers.html')
    else:
        miFormulario = Usuario_nuevo_Formulario(initial={'email': user.email})

    return render(request, 'editusers.html', {'miFormulario':miFormulario, 'user': user}) 
"""



@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            """
            form = PasswordChangeForm(usuario, data={
                'new_password1': input(f"Enter new password for user {usuario.password1}: "),
                'new_password2': input(f"Confirm new password for user {usuario.password2}: "),
            }) 
            """
            usuario.save()

            return render(request,"msj_usuario_editado.html" ,  {"mensaje":"Perfil editado con exito!"})

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario}) 




