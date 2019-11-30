from django.db import models

# Create your models here.


class Land(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    area = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
