from django.shortcuts import render

# Create your views here.
from .serializer import FloresSerializer, ArbolesSerializer
from .models import Flores, Arboles
from rest_framework import viewsets

class FloresViewset(viewsets.ModelViewSet):
    queryset=Flores.objects.all()
    serializer_class=FloresSerializer

class ArbolesViewset(viewsets.ModelViewSet):
    queryset=Arboles.objects.all()
    serializer_class=ArbolesSerializer