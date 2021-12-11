from django.db import models

# Create your models here.

class Strain(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    status = models.CharField(max_length=255)
    sort = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)
    crosses = models.CharField(max_length=255)
    breeder = models.CharField(max_length=255)
    effects = models.CharField(max_length=255)
    ailment = models.CharField(max_length=255)
    flavor = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    terpenes = models.CharField(max_length=255)
    thc = models.CharField(max_length=255)
    thca = models.CharField(max_length=255)
    thcv = models.CharField(max_length=255)
    cbd = models.CharField(max_length=255)
    cbda = models.CharField(max_length=255)
    cbdv = models.CharField(max_length=255)
    cbn = models.CharField(max_length=255)
    cbg = models.CharField(max_length=255)
    cbgm = models.CharField(max_length=255)
    cbgv = models.CharField(max_length=255)
    cbc = models.CharField(max_length=255)
    cbcv = models.CharField(max_length=255)
    cbv = models.CharField(max_length=255)
    cbe = models.CharField(max_length=255)
    cbt = models.CharField(max_length=255)
    cbl = models.CharField(max_length=255)