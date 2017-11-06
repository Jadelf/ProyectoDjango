from django.db import models
from django.utils import timezone


class Equipo(models.Model):
    author = models.ForeignKey('auth.User')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.CharField(max_length=3)
    especialidad=models.CharField(max_length=30)
    register_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
