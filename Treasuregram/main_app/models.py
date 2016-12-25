from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    img_loc = models.CharField(max_length=100, null=True)
