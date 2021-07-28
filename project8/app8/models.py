from django.db import models

# Create your models here.

class Product_Model(models.Model):
    pno = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=200)
    pprice = models.FloatField()
    pphoto = models.FileField()