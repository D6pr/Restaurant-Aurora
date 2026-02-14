from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at', 'delivery_method', 'payment_method')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'quantity', 'price')
    search_fields = ('dish__name',)
