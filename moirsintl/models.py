from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(default=False, max_length=200)
    product_description = models.TextField(default=False, max_length=200)
    product_category = models.CharField(max_length=100)
    product_tag = models.CharField(default=False, max_length=50)
    pub_date = models.DateTimeField('date published')
    product_img = models.ImageField(max_length=300)
    product_price = models.CharField(max_length=30000, default=False)
    product_status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = _("Product")
    def __unicode__(self):
        return _(u'%s') % self.product_name

    def __str__(self):
        return '{}'.format(self.product_name)

class Company(models.Model):
    company_intro = models.TextField(max_length=20000, verbose_name=_("Company Introduction"))
    company_about = models.TextField(max_length=20000, verbose_name=_("Company About"))
    company_service_title = models.TextField(max_length=20000, verbose_name=_("Company Service Title"))
    company_service_detail = models.TextField(max_length=20000, verbose_name=_("Company Service Detail"))
    company_status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Company Detail"
        verbose_name_plural = _("Company Detail")

    def __unicode__(self):
        return _(u'%s') % self.company_intro

    def __str__(self):
        return '{}'.format(self.company_intro)

