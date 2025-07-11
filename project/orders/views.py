from turtle import clear
from django.contrib import messages
from django.shortcuts import redirect, render

from favourite.favourite import add_to_favourite, clear_favourite, get_favourite, remove_from_favourite
from orders.models import Order
from main.models import Product
from users.models import User

# Create your views here.


def index(request):
    orders = Order.objects.all()

    # TODO: show only my
    # orders = Order.objects.filter(client=request.user)

    return render(request, "orders/index.html", {"orders": orders})


def confirm(request):

    items = get_favourite(request.session)

    if not items:
        messages.warning(request, "Your cart is empty!")
        return redirect("/favourite")

    products = Product.objects.filter(id__in=items.keys())

    Order.objects.create(
        total_price=sum(p.price for p in products),
        # client=User.objects.last()
    )

    clear_favourite(request.session)

    return redirect("/orders")