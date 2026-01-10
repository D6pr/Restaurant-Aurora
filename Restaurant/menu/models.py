from django.db import models

# Create your models here.

class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Закуски'),
        ('main', 'Основні страви'),
        ('dessert', 'Десерти'),
        ('drink', 'Напої'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='dishes/')
    popularity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
