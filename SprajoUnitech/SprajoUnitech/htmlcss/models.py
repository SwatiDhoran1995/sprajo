from django.db import models

# Create your models here.
class Sprajo(models.Model):
    Name = models.CharField(max_length=70)
    Image= models.ImageField(upload_to='uploads/')
    description = models.CharField(max_length=400)
    capacity = models.IntegerField()
    unit = models.CharField(max_length=5)
    price = models.IntegerField()

