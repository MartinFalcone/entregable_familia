# from unittest.util import _MAX_LENGTH
from django.db import models

# from entregable_familia.views import familia_template

# # # Create your models here.
class familia(models.Model):

    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_de_nacimiento=models.DateField()
