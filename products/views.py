from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from products.forms import ProductForm
from django.template import RequestContext,loader
from products.models import Product

def upload_file(request):
  if request.method == "POST":
    form = ProductForm(request.POST, request.Files)

    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/success/')

  else:
    form = ProductForm()

  return render(request, 'upload.html', {'form':form})

def products_list(request):
  products = Product.objects.all().order_by("product_name")
  #print products
  return render(request, 'products/products_list.html', {'product_list': products})

def product_detail(request, product_id):
  products = get_object_or_404(Product, pk=product_id)
  return render(request, 'products/product_detail.html', {'product': products})