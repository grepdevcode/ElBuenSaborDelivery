from django.db import models

# Create your models here.
class Persona(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=25)
    dni = models.CharField(max_length=10)
    email = models.CharField(max_length=30)

    class Meta:
        abstract = True



class Cliente(Persona):
    
    idCliente = models.AutoField(primary_key = True)
    


