from django.shortcuts import render
import os, json

from mainapp.models import Product, ProductCategory




MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekshop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)

