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
 

    # def update(self, instance, validated_data):
        
    
    def save(self, **kwargs):
        print("123111")
        return super().save(**kwargs)

    class Meta:
        model = ShortenedUrls
        fields = '__all__'
        fields = ["nick_name", "target_url"]