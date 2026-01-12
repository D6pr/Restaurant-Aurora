from django.urls import path
from .views import checkout_view, order_success, order_history, order_detail

urlpatterns = [
    path('checkout/', checkout_view, name='checkout'),
    path('success/<int:order_id>/', order_success, name='order_success'),
    path('history/', order_history, name='order_history'),
    path('detail/<int:order_id>/', order_detail, name='order_detail'),
]
