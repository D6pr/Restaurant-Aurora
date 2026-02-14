from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Повідомлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    is_processed = models.BooleanField(default=False, verbose_name="Оброблено")

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at}"