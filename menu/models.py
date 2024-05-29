from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=2083)
   
    
