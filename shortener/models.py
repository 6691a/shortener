import string
import random

from django.db import models
from base.models import BaseModels

from django.conf import settings

from plan.models import Plan

USER = settings.AUTH_USER_MODEL

class Organization(BaseModels):
    class Industries (models.TextChoices):
        PERSONAL = 'personal'
        RETAIL = 'retail'
        MANUFACTURING = 'manufacturing'
        IT = 'it'
        OTHERS = 'others'
    
    name = models.CharField(max_length=50)
    industry = models.CharField(max_length=15, choices=Industries.choices, default=Industries.OTHERS)
    plan = models.ForeignKey(Plan, on_delete=models.DO_NOTHING, null=True)


class Categories(BaseModels):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(USER, on_delete=models.CASCADE)

class ShortenedUrls(BaseModels):
    class UrlCreatedVia(models.TextChoices):
        WEBSITE = "web"
        TELEGRAM = "telegram"

    def rand_string():
        str_pool = string.digits + string.ascii_letters
        return ("".join([random.choice(str_pool) for _ in range(6)])).lower()
    
    def rand_letter():
        str_pool = string.ascii_letters
        return random.choice(str_pool).lower()

    nick_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)
    prefix = models.CharField(max_length=50)
    creator = models.ForeignKey(USER, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    create_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    expired_at = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ["-created_at"]
