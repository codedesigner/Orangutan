from django.shortcuts import render, get_object_or_404
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

def index(request, product_id):
  product_name = get_object_or_404(Product, pk=product_id)

  return render(request, 'products/index.html', {'product':product_name})