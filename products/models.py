from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='image/%Y/%m/%d')
    product_description = models.CharField(max_length=3000)

    def __unicode__(self):
        return self.product_name