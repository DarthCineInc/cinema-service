from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinemas.models import Cinema
from cinemas.serializers import CinemaSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def cinema_index(request):
    if request.method == "GET":
        return get_all_cinemas(request)
    if request.method == "POST":
        return create_cinema(request)

def get_all_cinemas(request):
    _ = request
    cinemas = Cinema.objects.all()
    serialized = CinemaSerializer(cinemas, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)

def create_cinema(request):
    cinema = CinemaSerializer(data=request.data)
    
    if Cinema.objects.filter(name=request.data.get('name', None)).exists():
        raise serializers.ValidationError("This cinema already exists")
    
    if cinema.is_valid():
        cinema.save()
        return Response(cinema.data, status=status.HTTP_201_CREATED)
    
    return Response(cinema.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def cinema_by_id(request, id: int):
    if request.method == "GET":
        return get_cinema_by_id(request, id)
    if request.method == "PUT":
        return update_cinema(request, id)
    
def get_cinema_by_id(request, id: int):
    _ = request
    cinema = Cinema.objects.filter(id=id).first()
    if not cinema:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(CinemaSerializer(cinema).data)

def update_cinema(request, id: int):
    cinema = Cinema.objects.filter(id=id).first()
    if not cinema:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CinemaSerializer(cinema, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
