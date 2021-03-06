from django.shortcuts import render
from django.template import loader
from django.template import context
# Create your views here.
from moirsintl.models import Product, Company


def index(request):
    template = loader.get_template('moirsintl/index.html')
    details = Company.objects.all()[0]
    context = {'details': details}
    return render(request, 'moirsintl/index.html', context)


def products(request):
    product = Product.objects.all()
    template = loader.get_template('moirsintl/product.html')
    context = { 'product' : product }
    return render(request, 'moirsintl/product.html', context)
    
