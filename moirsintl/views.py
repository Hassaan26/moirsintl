from django.shortcuts import render
from django.template import loader
# Create your views here.
from .models import Product


def index(request):
    latest_product_list = Product.objects.all()
    template = loader.get_template('moirsintl/product.html')
    context = {
        'latest_product_list': latest_product_list,
    }
    return render(request, 'moirsintl/product.html', context)

def contact(request):
    template = loader.get_template('moirsintl/contact.html')
    return render(request, 'moirsintl/contact.html')

def about(request):
    template = loader.get_template('moirsintl/about.html')
    return render(request, 'moirsintl/about.html')

def clients(request):
    template = loader.get_template('moirsintl/clients.html')
    return render(request, 'moirsintl/clients.html')

def services(request):
    template = loader.get_template('moirsintl/services.html')
    return render(request, 'moirsintl/services.html')
    
