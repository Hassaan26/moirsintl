from django.shortcuts import render
from django.template import loader
from django.template import context
# Create your views here.
from .models import Product, CompanyIntro, Service, ServiceDetail, Client


def index(request):
    template = loader.get_template('moirsintl/product.html')
    details = CompanyIntro.objects.all()[0]
    context = {'details': details}
    return render(request, 'moirsintl/product.html', context)

def contact(request):
    template = loader.get_template('moirsintl/contact.html')
    return render(request, 'moirsintl/contact.html')

def about(request):
    template = loader.get_template('moirsintl/about.html')
    return render(request, 'moirsintl/about.html')

def clients(request):
    template = loader.get_template('moirsintl/clients.html')
    cl_detail = Client.objects.all()[0]
    context = {'cl_detail' : cl_detail}
    return render(request, 'moirsintl/clients.html', context)

def services(request):
    service = Service.objects.all()
    ser_detail = ServiceDetail.objects.all()[0]
    template = loader.get_template('moirsintl/services.html')
    context = { 'service' : service , 'ser_detail': ser_detail }
    return render(request, 'moirsintl/services.html', context)
    
