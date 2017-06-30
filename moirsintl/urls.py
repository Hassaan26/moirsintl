from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^index/$', views.index, name='index'),
# url(r'^contact/$', views.contact, name='contact'),
# url(r'^about/$', views.about, name='about'),
# url(r'^services/$', views.services, name='services'),
# url(r'^clients/$', views.clients, name='clients'),
# url(r'^product/$', views.products, name='product')
    
]