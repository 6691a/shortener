from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import ShortenedUrls
from .serializers import ShortenerSerializers
from .utils import url_count_changer



class ShortenerlistCreateView(APIView):
    def get(self, request):
        urls = ShortenedUrls.objects.filter()

        serializer = ShortenerSerializers(urls, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ShortenerSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShortenerUpdateDeleteView(APIView):
    def put(self, request, id):
        urls = get_object_or_404(ShortenedUrls, id=id)
        # ShortenedUrls.objects.get(id=id, creator=request.user)

        serializer = ShortenerSerializers(urls, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # try:

    def delete(self, request, id):
        urls = get_object_or_404(ShortenedUrls, id=id)
        try:
            urls.delete()
        except Exception as e:
            print(e)
        else:
            url_count_changer(request, False)
            return Response(status=status.HTTP_204_NO_CONTENT)

