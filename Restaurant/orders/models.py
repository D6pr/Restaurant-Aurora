from django.db import models
from django.conf import settings
from menu.models import Dish

class Order(models.Model):
    DELIVERY_CHOICES = [
        ('courier', 'Кур’єр (+50 грн)'),
        ('pickup', 'Самовивіз'),
    ]
    PAYMENT_CHOICES = [
        ('cash', 'Готівка'),
        ('card_online', 'Картка онлайн'),
        ('card_on_delivery', 'Картка при отриманні'),
    ]

    STATUS_CHOICES = [
        ('pending', 'В процесі'),
        ('completed', 'Виконано'),
        ('cancelled', 'Скасовано'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_CHOICES)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.first_name} {self.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def get_total(self):
        return self.price * self.quantity
