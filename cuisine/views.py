# -*- coding: utf-8 -*-
from models import Restaurant
from django.shortcuts import render


def ViewAll(request):
    rest = Restaurant.objects.all()
    print(rest)
    return render(request, 'base.html', {'rest': rest})
