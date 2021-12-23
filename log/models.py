from django.db import models

from django.conf import settings

from base.models import BaseModels

USER = settings.AUTH_USER_MODEL

class BackOfficeLog(BaseModels):
    end_point = models.CharField(max_length=1000)
    method = models.CharField(max_length=10)
    body = models.JSONField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.DO_NOTHING)
    ip = models.CharField(max_length=20)
    status_code = models.IntegerField()

