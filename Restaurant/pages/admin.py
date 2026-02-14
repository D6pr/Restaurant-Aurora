from django.contrib import admin
from .models import Feedback

# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'email', 'message')