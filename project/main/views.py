from itertools import product
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .forms.rent import RentalForm
from .models import Product
from .forms.create import CreateProduct
from .forms.edit import EditProduct
from django.core.paginator import Paginator
from django.shortcuts import redirect


def index(request):
    products = Product.objects.all().order_by("id")
    return render(request, "index.html", {"products": products})



def catalog(request):
    products = Product.objects.all().order_by("id")

    page_number = request.GET.get("page", 1)
    page_size = request.GET.get("size", 5)

    page = Paginator(products, page_size).get_page(page_number)

    return render(
        request,
        "catalog.html",
        {"products": page.object_list, "total_count": len(products), "page": page},
    )



def rent(request):
    products = Product.objects.all().order_by("id")

    if request.method == "POST":
        form = RentalForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect("/catalog")

    else:
        form = RentalForm()

    return render(request, "rent.html", {"products": products, "form": form})




def create(request):
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!") 
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


