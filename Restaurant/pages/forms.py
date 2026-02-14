from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваше ім\'я'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваш email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваш відгук',
                'rows': 4
            }),
        }
        labels = {
            'name': "Ім'я",
            'email': "Email",
            'message': "Повідомлення"
        }