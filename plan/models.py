from django.db import models

from base.models import BaseModels
# Create your models here.
class Plan(BaseModels):
    name = models.CharField(max_length=20)
    print = models.IntegerField()

