
from django.contrib import admin
from django.urls import path
from app.views import saludo, perfil_usuario,ingresar_perfil,pasos,registro_proveedores, lista_proveedores,pasos_formulario



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo,name='home'),
   path('perfiles/',perfil_usuario,name='perfiles'),
   path('perfil_usuario/<int:id_entrada>', ingresar_perfil, name="ingresar_perfil"),
   path('pasos/',pasos,name="pasos"),
   path('proveedores/',registro_proveedores,name='proveedores'),
      path('lista_proveedores/',lista_proveedores,name='proveedores'),
      path('pasos_formulario/',pasos_formulario,name='pasos_formulario')
]
