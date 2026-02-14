from django.urls import path
from .views import about_view, home, contacts

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_view, name='about'),
    path('contacts/', contacts, name='contacts'),
]
