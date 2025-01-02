from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Coleccion, Elemento, TerminosLegales
from .serializers import ColeccionSerializer, ElementoSerializer, TerminosLegalesSerializer

class ColeccionViewSet(viewsets.ModelViewSet):
    queryset = Coleccion.objects.all()
    serializer_class = ColeccionSerializer

class ElementoViewSet(viewsets.ModelViewSet):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer

class TerminosLegalesViewSet(viewsets.ModelViewSet):
    queryset = TerminosLegales.objects.all()
    serializer_class = TerminosLegalesSerializer
