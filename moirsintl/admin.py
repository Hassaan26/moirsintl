from django.contrib import admin
from .models import Product, CompanyIntro, Service, ServiceDetail

# Register your models here.

admin.site.register(Product)
admin.site.register(CompanyIntro)
admin.site.register(Service)
admin.site.register(ServiceDetail)
