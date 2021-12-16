from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect

from statistic.models import Statistic
from ratelimit.decorators import ratelimit


from .models import ShortenedUrls
from .serializers import ShortenerSerializers
from .utils import url_count_changer


class UrlRedirectView(APIView):
    # @ratelimit(key='ip', rate='10/s')
    def get(self, request, prefix, url):
        url = get_object_or_404(ShortenedUrls, prefix=prefix, shortened_url=url)
        is_permanent = False
        target = url.target_url
        if url.creator.organization:
            is_permanent = True

        if not target.startswith("https://") and not target.startswith("http://"):
            target = f"https://{url.target_url}"
        custom_params = request.GET.dict() if request.GET.dict() else None
        print("1")
        statistic = Statistic()
        statistic.record(request, url, custom_params)
        return redirect(target, permanent=is_permanent)


class ShortenerListCreateView(APIView):
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



# def url_redirect(request, prefix, url):
    # print(prefix, url)
