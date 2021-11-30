from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=20)
    print = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
