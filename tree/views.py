from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StrainsSerializer
from .models import Strain


class StrainsList(viewsets.ModelViewSet):
    queryset = Strain.objects.all()[0:5]
    serializer_class = StrainsSerializer