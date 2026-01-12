from django.shortcuts import get_object_or_404, redirect, render
from cart.models import CartItem
from menu.models import Dish

# Create your views here.

def menu_view(request):
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    dishes = Dish.objects.all()

    if category:
        dishes = dishes.filter(category=category)

    if sort == 'price':
        dishes = dishes.order_by('price')
    elif sort == 'popularity':
        dishes = dishes.order_by('-popularity')
    elif sort == 'new':
        dishes = dishes.order_by('-created_at')

    return render(request, 'menu/menu.html', {'dishes': dishes})

