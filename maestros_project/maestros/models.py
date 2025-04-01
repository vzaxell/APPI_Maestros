from django.db import models

class Maestro(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    materia = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
