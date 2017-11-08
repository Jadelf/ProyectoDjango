from django.db import models
from django.utils import timezone
from django.contrib import admin

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
    edad=models.IntegerField()
    especialidad=models.CharField(max_length=30)
    register_date=models.DateTimeField(default=timezone.now)
    equipos=models.ManyToManyField(Equipo,through='Reservacion')
    def __str__(self):
        return self.nombre

class Reservacion(models.Model):
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)

class ReservacionInLine(admin.TabularInline):
    model = Reservacion
    extra = 1

class MedicoAdmin(admin.ModelAdmin):
    inlines = (ReservacionInLine,)

class EquipoAdmin(admin.ModelAdmin):
    inlines = (ReservacionInLine,)
