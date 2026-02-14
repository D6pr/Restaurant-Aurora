from django.db import models
from django.conf import settings
from menu.models import Dish, DishOption

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    options = models.ManyToManyField(DishOption, blank=True)

    def get_total_price(self):
        base = self.dish.price * self.quantity
        extras = sum(opt.price for opt in self.options.all()) * self.quantity
        return base + extras