# myapp/views.py
from django.shortcuts import render

def welcome_view(request):
    return render(request, 'dashboard/welcome.html')

def home_view(request):
    return render(request, 'dashboard/home.html')
