from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    context = {
        'date': datetime.date.today(),
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    return render(request, 'mainapp/products.html')