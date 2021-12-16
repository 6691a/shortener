from django.db import models
from django.conf import settings
from django.db.models.base import Model

from shortener.models import ShortenedUrls
from base.models import BaseModels

USER = settings.AUTH_USER_MODEL

class TrackingParams(BaseModels):
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    shortened_url = models.ForeignKey(ShortenedUrls, on_delete=models.CASCADE)
    params = models.CharField(max_length=20)

    @classmethod
    def get_tracking_params(cls, author, shortened_url_id: int):
        return cls.objects.filter(author=author, shortened_url_id=shortened_url_id).values_list("params", flat=True)
