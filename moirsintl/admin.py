from django.contrib import admin
from .models import Product, CompanyIntro, Service, ServiceDetail,Client

# Register your models here.

admin.site.register(Product)
admin.site.register(CompanyIntro)
admin.site.register(Service)
admin.site.register(ServiceDetail)
admin.site.register(Client)