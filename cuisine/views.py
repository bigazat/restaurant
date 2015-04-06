# -*- coding: utf-8 -*-
from models import Restaurant


def ViewAll(request):
    rest = Restaurant.objects.all()
    print(rest)

