from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Product
from .forms.create import CreateProduct
from .forms.edit import EditProduct


def index(request):
    return render(request, "index.html")

def catalog(request):
    products = Product.objects.all()
    return render(request, "catalog.html", {"products": products, "count": len(products)})


def create(request):
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")  # ✅ тепер це працюватиме
            return redirect('home')
    else:
        form = CreateProduct()
    return render(request, 'create.html', {'form': form})

def edit(request, id):
    product = Product.objects.get(id=id)

    if product is None:
        return HttpResponse("Product not found")

    form = EditProduct(instance=product)

    if request.method == "POST":
        form = EditProduct(request.POST, request.FILES, instance=product)
        form.save()
        return redirect("/catalog")

    return render(request, "edit.html", {"form": form})

def delete(request, id):
    if id <= 0:
        return HttpResponse("Invalid ID")

    itemToDelete = get_object_or_404(Product, pk=id)

    itemToDelete.delete()

    return redirect("/catalog")

def details(request, id):
    if id <= 0:
        return HttpResponse("Invalid ID")
    itemToDetail = get_object_or_404(Product, pk=id)
    return render(request, 'car_details.html', {'item': itemToDetail})



    
