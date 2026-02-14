from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from menu.models import Dish, DishOption
from django.contrib.auth.decorators import login_required


@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

@login_required
def add_to_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    quantity = int(request.POST.get("quantity", 1))
    option_ids = request.POST.getlist("options")
    options = DishOption.objects.filter(id__in=option_ids)

    item = CartItem.objects.create(user=request.user, dish=dish, quantity=quantity)
    item.options.set(options)
    item.save()

    return redirect("cart")



@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

@login_required
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == "POST":
        qty = int(request.POST.get("quantity", 1))
        item.quantity = qty
        item.save()
    return redirect('cart')

from django.http import JsonResponse

@login_required
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == "POST":
        qty = int(request.POST.get("quantity", 1))
        item.quantity = qty
        item.save()
        cart_total = sum(i.get_total_price() for i in CartItem.objects.filter(user=request.user))
        return JsonResponse({
            "item_total": float(item.get_total_price()),
            "cart_total": float(cart_total)
        })
    return redirect('cart')
