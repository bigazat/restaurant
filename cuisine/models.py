# -*- coding: utf-8 -*-
from django.db import models


class Restaurant(models.Model):
    name =  models.CharField(max_length=254, verbose_name=u"Name")
    address = models.TextField(blank=True, verbose_name=u"Address")
    phone = models.CharField(max_length=12, blank=True, verbose_name=u"Phone")
    cuisine = models.TextField(blank=True, verbose_name=u"Cuisine")

    def __unicode__(self):
        return u"%s" % self.name