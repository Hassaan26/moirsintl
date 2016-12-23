from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_info = models.CharField(max_length=200)
    company_description = models.CharField(max_length=500)
    company_status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "companies"