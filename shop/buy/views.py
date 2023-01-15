from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'buy/index.html')


def about(request):
    return render(request, 'buy/index.html')


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
