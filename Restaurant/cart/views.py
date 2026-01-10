from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from menu.models import Dish
from django.contrib.auth.decorators import login_required


@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

def add_to_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    item, created = CartItem.objects.get_or_create(user=request.user, dish=dish)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('cart')

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == "POST":
        qty = int(request.POST.get("quantity", 1))
        item.quantity = qty
        item.save()
    return redirect('cart')
