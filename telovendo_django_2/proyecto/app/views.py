from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import PerfilUsuario, Proveedores
from app.forms import ProveedoresForm

def lista_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request,'lista_proveedores.html',{'proveedores':proveedores})

def saludo(request):
    return render(request, "pasos_g2.html")

# Create your views here.
def perfil_usuario(request):
    perfiles = PerfilUsuario.objects.all()
    return render(request,'perfiles.html',{'perfiles':perfiles})


def ingresar_perfil(request,id_entrada):
    perfil = PerfilUsuario.objects.get(user_id=id_entrada)
    context ={ 'perfil' : perfil}
    return render (request, 'perfil_usuario.html', context)
def pasos(request):
    return render (request, 'pasos_g3.html')


def registro_proveedores(request):
    if request.method=='POST':
        proveedor_formulario = ProveedoresForm(request.POST)

        if proveedor_formulario.is_valid():
            proveedor_formulario.save()
            return redirect('/lista_proveedores')
            

    else:
        formulario_proveedor = ProveedoresForm()
        context={'formulario':formulario_proveedor}
        return render(request,'proveedores.html',context)

def pasos_formulario(request):
    return render (request,'pasos_g4.html')   

 