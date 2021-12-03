from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        urls = ShortenedUrls.objects.get(id=id, creator=request.user)
        if not urls.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # try:

    def delete(self, request):
        urls = ShortenedUrls.objects.get(id=id, creator=request.user)
        if not urls.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            urls.delete()
        except Exception:
            print(Exception)
        else:
            url_count_changer
