from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING
from django.conf import settings

from plan.models import Plan
from shortener.models import Organization

USER = settings.AUTH_USER_MODEL

class User(AbstractUser):
    plan = models.ForeignKey(Plan, on_delete=DO_NOTHING, verbose_name="요금", null=True)
    url_count = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization, on_delete=DO_NOTHING, null=True)


class EmailVerification(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)