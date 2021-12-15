from django.db import models
from base.models import BaseModels
from shortener.models import ShortenedUrls
from django.contrib.gis.geoip2 import GeoIP2


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
    country_code = models.CharField(max_length=2, default="XX")
    country_name = models.CharField(max_length=100, default="UNKNOWN")

    def record(self, request, url: ShortenedUrls):
        self.shortened_url = url
        self.ip = request.META["REMOTE_ADDR"]
        self.web_browser = request.user_agent.browser.family
        self.device = self.ApproachDevice.MOBILE if request.user_agent.is_mobile else self.ApproachDevice.TABLET if request.user_agent.is_tablet  else self.ApproachDevice.PC
        self.device_os = request.user_agent.os.family
        try: 
            country = GeoIP2().country(self.ip)
            self.country_code = country.get("country_code", "XX")
            self.country_name = country.get("country_name", "UNKNOWN")
        except:
            pass
        url.clicked()
        self.save()
