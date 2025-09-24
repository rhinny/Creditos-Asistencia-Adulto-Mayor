from django.db import models

# Create your models here.

class Estudiante_log(models.Model):
    correo_estudiante = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50) #relacionarla con la base de datos

    def __str__(self):
        return f"{self.correo_estudiante} ({self.contraseña})"
    
class