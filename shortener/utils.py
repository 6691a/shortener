from django.db.models import F
from .models import ShortenedUrls
from user.models import User


def url_count_changer(request, is_increase: bool):
    count_number = 1 if is_increase else -1
    # request.user.objects.update(url_count=F('url_count') + count_number)
    User.objects.filter(id=1).update(url_count=F('url_count') + count_number)