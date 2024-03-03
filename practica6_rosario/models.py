from django.db import models

# Create your models here.
class Flores(models.Model):
    nombre = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    significado = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30, choices=[("Pequeña", "Pequeña"), ("Mediana", "Mediana"), ("Grande", "Grande")])
    fecha_creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}--{self.color}--{self.fecha_creado}"
class Arboles(models.Model):
    nombre = models.CharField(max_length = 20)
    tamaño = models.CharField(max_length = 20, choices=[("Pequeño", "Pequeño"), ("Mediano", "Mediano"), ("Grande", "Grande")])
    tamañom = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}--{self.tamañom}"