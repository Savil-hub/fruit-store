from django.shortcuts import render
from .models import Product

def online_store(request):
    return render(request, "online_shopping.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'online_shopping.html', {'products': products})