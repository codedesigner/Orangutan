from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='image/%Y/%m/%d')
    product_descrition = models.CharField(max_length=3000)