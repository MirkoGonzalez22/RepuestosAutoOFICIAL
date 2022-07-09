from django.db import models

# Create your models here.

class Repuestos(models.Model):
    id = models.CharField(max_length=6, primary_key=True, verbose_name='id')
    serial = models.CharField(max_length=25, verbose_name='serial')
    marca = models.CharField(max_length=25, null=True, blank=True, verbose_name='marca')
    