from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING

from shortener.models import Plan

class User(AbstractUser):
    plan = models.ForeignKey(Plan, on_delete=DO_NOTHING, verbose_name="요금", null=True)
