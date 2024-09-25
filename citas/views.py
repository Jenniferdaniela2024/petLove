from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import clientes
from .forms import clientesForm

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request,'paginas/index.html')
    else:
        dates = User.objects.get(username = request.POST['User'])
        if(dates.check_password(request.POST['password'])):
            return redirect('index')#este es el index
             
        else:
            return render(request,'paginas/index.html',{
                'message':'La contraseña o usuarios no coinciden'
            })
        

def index(request):
    return render(request, 'paginas/inicio.html') #Aqui haremos el formulario

def Clientes(request):
    Clientes = clientes.objects.all()  # Obtén todos los clientes
    return render(request, 'Clientes/index.html', {'clientes': Clientes})  # Usa un diccionario

def crear(request):
    formulario = clientesForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Clientes')
    return render(request, 'Clientes/crear.html', {'formulario': formulario})

def editar(request, identificacion_cliente):
    cliente = clientes.objects.get(identificacion_cliente=identificacion_cliente)
    formulario = clientesForm(request.POST or None, instance=cliente)    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Clientes')
    return render(request, 'Clientes/editar.html', {'formulario': formulario})


def eliminar(request, identificacion_cliente):
    cliente = clientes.objects.get(identificacion_cliente=identificacion_cliente)
    if  cliente.delete():
       
        return render(request, 'Clientes/index.html', {'mensaje':'Cliente borrado'} )  # Cambiado para redirigir a la lista de clientes


def Mascotas(request):
    return render(request, 'Mascotas/index.html' )