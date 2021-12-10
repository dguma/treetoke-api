# from django.db import models
from rest_framework import serializers
from .models import Strain

class StrainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strain
        fields = ('id', 'status', 'sort', 'name', 'slug', 'image', 'description', 'type', 'crosses', 'breeder', 'effects', 'ailment', 'flavor', 'location', 'terpenes', 'thc', 'thca', 'thcv', 'cbd', 'cbda', 'cbdv', 'cbn', 'cbg', 'cbgm', 'cbgv', 'cbc', 'cbcv', 'cbv', 'cbe', 'cbt','cbl')