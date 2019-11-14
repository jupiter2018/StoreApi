from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ManufacturerSerializer, ShoeSerializer, ShoeTypeSerializer, ShoeColorSerializer
from .models import Manufacturer, Shoe, ShoeType, ShoeColor
# Create your views here.

class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
