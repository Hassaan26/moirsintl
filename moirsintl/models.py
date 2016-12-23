from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    product_status = models.BooleanField(default=True)