from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Product

def index(request):
    return render(request, "index.html")

def catalog(request):
    products = Product.objects.all()
    return render(request, "catalog.html", {"products": products, "count": len(products)})

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
