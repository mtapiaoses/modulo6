
from django.contrib import admin
from django.urls import path
from app.views import saludo, perfil_usuario,ingresar_perfil,pasos,registro_proveedores



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo,name='home'),
   path('perfiles/',perfil_usuario,name='perfiles'),
   path('perfil_usuario/<int:id_entrada>', ingresar_perfil, name="ingresar_perfil"),
   path('pasos/',pasos,name="pasos"),
   path('proveedores/',registro_proveedores,name='proveedores')
]
