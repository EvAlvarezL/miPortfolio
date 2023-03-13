from django.db import models

# Create your models here.

class Proyectos(models.Model):
    nombre=models.CharField(max_length=50)
    link=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='proyectos')

    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'

    def __str__(self):
        return self.nombre
