from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class tablCategoria(models.Model):
    categNombre = models.CharField(max_length = 100)
    categDescrip = models.CharField(max_length = 300)
    categActivo = models.CharField(max_length = 2)

class tablSubCategoria(models.Model):
    subCategNombre=models.CharField(max_length = 100)
    subCategCateg=models.ForeignKey(tablCategoria, on_delete = models.CASCADE)
    subCategDescrip=models.TextField()
    subCategActivo=models.CharField(max_length = 2)

class tablMarca(models.Model):
    marcaNombre=models.CharField(max_length = 100)
    marcaActiva=models.CharField(max_length = 2)

class tablModelo(models.Model):
    modeloNombre=models.CharField(max_length = 100)
    modeloMarca=models.ForeignKey(tablMarca, on_delete = models.CASCADE)
    modeloActivo=models.CharField(max_length = 2)