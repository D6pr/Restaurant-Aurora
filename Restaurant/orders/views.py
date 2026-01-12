from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from cart.models import CartItem
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import OrderForm

def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        messages.error(request, "Ваш кошик порожній.")
        return redirect('cart')

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            total = sum(item.get_total_price() for item in cart_items)
            if order.delivery_method == 'courier':
                total += 50
            order.total_price = total
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    dish=item.dish,
                    quantity=item.quantity,
                    price=item.dish.price
                )
            cart_items.delete()

            messages.success(request, f"Замовлення прийнято! Номер замовлення: {order.id}")
            return redirect('order_success', order_id=order.id)
        else:
            messages.error(request, "Помилка оформлення. Перевірте введені дані.")
    else:
        form = OrderForm()

    total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'orders/checkout.html', {'form': form, 'cart_items': cart_items, 'total': total})

def order_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/success.html', {'order': order})

@login_required
def order_history(request):
    status = request.GET.get('status')
    date = request.GET.get('date')

    orders = Order.objects.filter(user=request.user)

    if status:
        orders = orders.filter(status=status)
    if date:
        orders = orders.filter(created_at__date=date)

    return render(request, 'orders/history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})
