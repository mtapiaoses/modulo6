
from django.contrib import admin
from django.urls import path
from app.views import (saludo, perfil_usuario, ingresar_perfil, 
pasos, registro_proveedores, lista_proveedores,Login_Usuario
,pasos_formulario, Login_Usuario, logout_view,logueo_exitoso,lanza_inicio)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lanza_inicio, name='home'),
    path('perfiles/', perfil_usuario, name='perfiles'),
    path('perfil_usuario/<int:id_entrada>',
         ingresar_perfil, name="ingresar_perfil"),
    path('pasos/', pasos, name="pasos"),
    path('proveedores/', registro_proveedores, name='proveedores'),
    path('lista_proveedores/', lista_proveedores, name='proveedores'),
    path('pasos_formulario/', pasos_formulario, name='pasos_formulario'),
    path('login/',Login_Usuario.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logueo_exitoso/',login_required(logueo_exitoso),name='logueo_exitoso' )
]



