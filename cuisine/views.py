# -*- coding: utf-8 -*-
from models import Restaurant
from django.shortcuts import render, get_object_or_404


def ViewAll(request):
    rest = Restaurant.objects.all()
    print(rest)
    return render(request, 'base.html', {'rest': rest})

def ViewRest(request, rest_id):
    rest =  get_object_or_404(Restaurant, pk=rest_id)
    return render(request, 'view_rest.html', {'rest': rest})
