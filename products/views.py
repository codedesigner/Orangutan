from django.shortcuts import render
from django.http import HttpResponseRedirect
from products.forms import ProductForm

def upload_file(request):
  if request.method == "POST":
    form = ProductForm(request.POST, request.Files)

    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/success/')

  else:
    form = ProductForm()

  return render(request, 'upload.html', {'form':form})
