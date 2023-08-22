from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from MAIN.models import Entradas_Blog
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from PROFILE.models import Avatar
from PROFILE.views import agregarAvatar


@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    #if  avatares is True:
    return render(request, 'inicio.html', {'url':avatares[0].imagen.url})
    #else:
        #return render(request, 'inicio.html')

"""   
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if agregarAvatar is True:
        return render(request,'inicio.html', {'url':avatares[0].imagen.url})
    
    else:
        return render(request,'inicio2.html')
  
"""        


#def signup(request):
    #return render(request,'signup.html')

def about(request):
    return render(request,'about.html')
@login_required
def blogs(request):
    return render(request,'blogs.html')

def blog_1(request):
    return render(request,'blog_1.html')

def blog_2(request):
    return render(request,'blog_2.html')

def blog_3(request):
    return render(request,'blog_3.html')



class Entradas_list(ListView):
    model =Entradas_Blog
    template_name = 'blogs_list.html'



class Entradas_creacion(CreateView):
    model = Entradas_Blog
    template_name = "blog_creacion.html"
    success_url = reverse_lazy("entradas_list")
    fields = '__all__'


class Entradas_detalle(DetailView):
    model = Entradas_Blog
    template_name = 'blogs_detalle.html'


class Entradas_delete(DeleteView):
    model = Entradas_Blog
    success_url = reverse_lazy("entradas_list")


class Entradas_update(UpdateView):
    model = Entradas_Blog
    success_url = reverse_lazy('entradas_list')
    fields = ['Nombre', 'Fecha', 'Titulo', 'Subtitulo', 'Post']

