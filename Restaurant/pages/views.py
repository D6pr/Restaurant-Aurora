from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages

def home(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contacts(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Дякуємо за ваш відгук! Ми зв\'яжемося з вами найближчим часом.')
            return redirect('contacts')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = FeedbackForm()
    
    return render(request, 'pages/contacts.html', {'form': form})