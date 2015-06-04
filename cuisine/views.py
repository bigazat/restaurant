# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Restaurant
from serializers import RestSerializer
# from django.shortcuts import render, get_object_or_404


@api_view(['GET', 'POST'])
def restaurant_list(request):
    """
    List all restaurants, or create a new restaurant.
    """
    if request.method == 'GET':
        rest = Restaurant.objects.all()
        serializer = RestSerializer(rest, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RestSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, pk):
    """
    Get, udpate, or delete a specific restaurant
    """
    try:
        rest = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestSerializer(rest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestSerializer(rest, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# def restaurant_list(request):
#    rest = Restaurant.objects.all()
#    print(rest)
#    return render(request, 'base.html', {'rest': rest})

# def restaurant_detail(request, rest_id):
#    rest =  get_object_or_404(Restaurant, pk=rest_id)
#    return render(request, 'view_rest.html', {'rest': rest})
