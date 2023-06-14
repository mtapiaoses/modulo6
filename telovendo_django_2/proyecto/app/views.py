from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import PerfilUsuario, Proveedores
from app.forms import ProveedoresForm, FormularioLogin
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout

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

    
class Login_Usuario(TemplateView):
    def get(self, request, *args, **kwargs):
        formulario_login = FormularioLogin()
        context={'formulario_login':formulario_login}
        return render(request, 'login.html',context)

    def post(self, request, *args, **kwargs):
        print(request.POST['usuario'])
        print(request.POST['password'])
        formulario_login = FormularioLogin(request.POST)
        if formulario_login.is_valid():
            print("pase el login")
            usuario = formulario_login.cleaned_data['usuario']
            password = formulario_login.cleaned_data['password']
            print(usuario)    
            usuario = authenticate(request,username=usuario,password=password)
            print(usuario)
            if usuario is not None:
                login(request,usuario)
                return redirect('/logueo_exitoso/')

    
       
        return redirect('/')

def logout_view(request):
        print(f"momento previo : {request.user}")
        logout(request)
        print(f"momento de la salida : {request.user}")
        return redirect('login')
 
def logueo_exitoso(request):
    perfil=PerfilUsuario.objects.get(user_id=request.user.id)
    context = {'perfil': perfil }
    return render(request,'logueo_exitoso.html',context)
                      

            
def lanza_inicio(request):
    return render(request,'inicio.html')



#PRUEBA DE LOGIN CON FUNCION
# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


   

 

