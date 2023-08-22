from django.db import models


class Usuario_nuevo(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Email {self.email} - Password {self.password}" #se crean solo en models y funcionan
    