from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.first_name} | {self.user.last_name} | {self.edad} | {self.ciudad} "

class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)    

      
    def __str__(self):
        return f"{self.nombre} | {self.rut} | {self.email} | {self.telefono} | {self.telefono} "