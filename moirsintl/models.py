from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    product_status = models.BooleanField(default=True)

class CompanyIntro(models.Model):
    company_intro = models.TextField(max_length=20000, verbose_name=_("Company Detail"))
    company_status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Company Detail"
        verbose_name_plural = _("Company Detail")

    def __unicode__(self):
        return _(u'%s') % self.company_intro

    def __str__(self):
        return '{}'.format(self.company_intro)

class Service(models.Model):
    service_type = models.TextField(max_length=20000, verbose_name=_("Service Type"))
    service_type_detail = models.TextField(max_length=20000, verbose_name=_("Service Type Detail"))
    service_status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = _("Services")

    def __unicode__(self):
        return _(u'%s') % self.service_type

    def __str__(self):
        return '{}'.format(self.service_type)

class ServiceDetail(models.Model):
    service_detail = models.TextField(max_length=20000, verbose_name=_("Service Detail"))
    class Meta:
        verbose_name = "Service Detail"
        verbose_name_plural = _("Service Detail")

    def __unicode__(self):
        return _(u'%s') % self.service_detail

    def __str__(self):
        return '{}'.format(self.service_detail)


class Client(models.Model):
    client_detail = models.TextField(max_length=20000, verbose_name=_("Client Detail"))
    class Meta:
        verbose_name = "Client Detail"
        verbose_name_plural = _("Client Detail")

    def __unicode__(self):
        return _(u'%s') % self.client_detail

    def __str__(self):
        return '{}'.format(self.client_detail)