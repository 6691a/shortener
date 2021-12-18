from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action, renderer_classes
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from .utils import url_count_changer
from .models import ShortenedUrls
from .serializers import ShortenerSerializers


class UrlViewSet(viewsets.ModelViewSet):
    queryset = ShortenedUrls.objects.order_by('created_at')
    serializer_class = ShortenerSerializers
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        # POST METHOD
        serializer = ShortenerSerializers(data=request.data)
        serializer.is_valid(True)
        obj = serializer.create(request, serializer.data)
        return Response(ShortenerSerializers(obj).data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        # Detail GET
        queryset = self.get_queryset().filter(pk=pk).first()
        serializer = ShortenerSerializers(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # PUT METHOD
        pass

    def partial_update(self, request, pk=None):
        # PATCH METHOD
        pass

    @renderer_classes([JSONRenderer])
    def destroy(self, request, pk=None):
        # DELETE METHOD
        queryset = self.get_queryset().filter(pk=pk, creator_id=request.user.id)
        if not queryset.exists():
            raise Http404
        queryset.delete()
        url_count_changer(request, False)
        return Response(status=status.HTTP_201_CREATED)
    
    def list(self, request):
        # GET ALL
        queryset = self.get_queryset().all()
        serializer = ShortenerSerializers(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def add_click(self, request, pk=None):
        # query_set = self.get_queryset().filter(pk=pk, creator_id=request.user.id)
        query_set = get_object_or_404(self.get_queryset(), pk=pk)
        obj = query_set.clicked()
        serializer = ShortenerSerializers(obj)
        return Response(serializer.data)