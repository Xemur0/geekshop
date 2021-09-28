from django.shortcuts import render
import os, json

from mainapp.models import Product




MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    # file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'geekshop',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)

