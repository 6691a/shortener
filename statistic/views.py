from datetime import datetime, timedelta
from django.db.models import Count, query

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from django.shortcuts import  get_object_or_404
from django.http.response import Http404

from shortener.models import ShortenedUrls
from .models import Statistic
from .serializers import BrowserStatSerializer, DateStatSerializer

class DateStatView(APIView):
    def get(self, reqeust, url_id: int):
        url = get_object_or_404(ShortenedUrls, id=url_id)
        target_obj = Statistic.objects.filter(
            shortened_url_id=url_id, 
            created_at__gte=datetime.utcnow() + timedelta(hours=9)  - timedelta(days=14)
        )

        clicks = (
            target_obj.values("created_at__date")
            .annotate(clicks=Count("id"))
            .values("shortened_url__target_url", "shortened_url__shortened_url", "created_at__date", "clicks")
            .order_by("created_at__date")
        )
        serializer = DateStatSerializer(clicks, many=True)

        return Response(serializer.data)

class BrowserStatView(APIView):
    def get(self, reqeust, url_id: int):
        query_set = Statistic.objects.filter(
            shortened_url_id=url_id,
            # shortened_url__creator_id=reqeust.user.id,
            shortened_url__creator_id=1,
            created_at__gte=datetime.utcnow() + timedelta(hours=9)  - timedelta(days=14)
        )
        if not query_set.exists():
            raise Http404
        browers = (
            query_set.values("web_browser", "created_at__date")
            .annotate(count=Count("id"))
            .values("count", "web_browser", "created_at__date")
            .order_by("-created_at__date")
        )
        browers = (
            query_set.values("web_browser")
            .annotate(count=Count("id"))
            .values("count", "web_browser")
            .order_by("-count")
        )
        serializer = BrowserStatSerializer(browers, many=True)
        return Response(serializer.data)