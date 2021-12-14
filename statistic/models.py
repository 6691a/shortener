from django.db import models
from base.models import BaseModels
from shortener.models import ShortenedUrls

class Statistic(BaseModels):
    class ApproachDevice(models.TextChoices):
        PC = "pc"
        MOBILE = "MOBILE"
        TABLET = "TABLET"
    
    shortened_url = models.ForeignKey(ShortenedUrls, on_delete=models.CASCADE)
    ip = models.CharField(max_length=15)
    web_browser = models.CharField(max_length=50)
    device = models.CharField(max_length=6, choices=ApproachDevice.choices)
    device_os = models.CharField(max_length=30)
    country_code = models.CharField(max_length=2)    
    country_name = models.CharField(max_length=100)    

