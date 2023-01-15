from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    sSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': sSlides, 'range': range(1, sSlides), 'product': products}
    return render(request, 'buy/index.html', params)


def about(request):
    return render(request, 'buy/about.html')


def contact(request):
    return render(request, 'buy/index.html')


def tracker(request):
    return render(request, 'buy/index.html')


def search(request):
    return render(request, 'buy/index.html')


def productview(request):
    return render(request, 'buy/index.html')


def checkout(request):
    return render(request, 'buy/index.html')
