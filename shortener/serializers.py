from rest_framework import serializers

from .utils import url_count_changer
from .models import ShortenedUrls

class ShortenerSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context['request']
        instance = ShortenedUrls.objects.create(
            creator_id=1,
            **validated_data
        )
        url_count_changer(request, True)
        return instance
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


    class Meta:
        model = ShortenedUrls
        fields = '__all__'
        fields = ["id", "category", "prefix", "creator", "nick_name", "target_url", "shortened_url", "click"]
        extra_kwargs = {
            "category": {"write_only": True},
            "prefix": {"read_only": True},
            "shortened_url": {"read_only": True},
        }