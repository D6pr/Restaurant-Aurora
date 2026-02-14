from django.contrib import admin
from .models import Dish, DishOption

class DishOptionInline(admin.TabularInline):
    model = DishOption
    extra = 1

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "popularity", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("name", "description")
    inlines = [DishOptionInline]
