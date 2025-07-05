from django.shortcuts import redirect, render
from django.contrib import messages

from favourite.favourite import add_to_favourite, clear_favourite, get_favourite, remove_from_favourite
from main.models import Product

def index(request):
    items = get_favourite(request.session)
    products = Product.objects.filter(id__in=items.keys())

    return render(request, "favourite/index.html", {"products": products})


def add(request, id, quantity=1):
    if Product.objects.get(id=id) is None:
        messages.error(request, "Car not found!")
        return redirect("/favourite")

    add_to_favourite(request.session, id, quantity)
    messages.success(request, "Car added to favourite list!")

    return redirect("/favourite")

def remove(request, id):
    if Product.objects.get(id=id) is None:
        messages.error(request, "Car not found!")
        return redirect("/favourite")

    remove_from_favourite(request.session, id)
    messages.success(request, "Car removed from favourite list!")

    return redirect("/favourite")


def clear(request):
    clear_favourite(request.session)
    messages.success(request, "Favourite list cleared!")

    return redirect("/favourite")

# def remove(request, id):



   