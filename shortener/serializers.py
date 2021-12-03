from django.db import models
from rest_framework import serializers

from .models import ShortenedUrls
class ShortenerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrls