from django.db import models

# Create your models here.

class Estudiante_log(models.Model):
    correo_estudiante = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50) #relacionarla con la base de datos,
    rol = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f"{self.correo_estudiante} ({self.rol})"
    
class AdultoM_log(models.Model):
    correo_adulto = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    rut = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f"{self.correo_adulto} ({self.rut})"

class Cita(models.Model):
    id_cita=models.AutoField(primary_key=True)
    correo_adulto= models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante_log, on_delete=models.CASCADE)
    fecha_inicio= models.DateField() #API
    fecha_termino= models.DateField() #API

    def __str__(self):
        return f"cita con: {self.correo_estudiante} - ({self.rol})"


