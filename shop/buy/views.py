from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
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
