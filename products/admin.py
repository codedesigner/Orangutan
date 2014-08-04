from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
  fieldsets = [
      ('Product Name',       {'fields':['product_name']}),
      ('Image',      {'fields':['product_image']}),
      ('Description',{'fields':['product_description'], 'classes' : ['collapse']}),
  ]

  list_display = ('product_name', 'product_image', 'product_description')

admin.site.register(Product, ProductAdmin)