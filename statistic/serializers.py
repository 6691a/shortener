from rest_framework import serializers


class DateStatSerializer(serializers.Serializer):
    # url = serializers.
    shortened_url__target_url = serializers.CharField()
    shortened_url__shortened_url = serializers.CharField()
    created_at__date = serializers.DateField(format="%Y-%m-%d")
    clicks = serializers.IntegerField()
    
class BrowerStatSerializer(serializers.Serializer):
    web_browser = serializers.CharField(max_length=50)
    count = serializers.IntegerField()
    date = serializers.DateField(source='created_at__date', required=False)
