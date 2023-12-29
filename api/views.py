from django.shortcuts import render
from rest_framework import viewsets
from api.models import Cities
from api.serializers import CitySerializer
# Create your views here.


class CityViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer
