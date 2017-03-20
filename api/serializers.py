from rest_framework import serializers
from shortener.validators import validate_url
from shortener.models import KbsURL

class UrlSerializer(serializers.ModelSerializer):
    shortcode = serializers.SerializerMethodField('get_short_url')
    
    def get_short_url(self, obj):
        return obj.get_short_url()

    def validate(self, data):
        validate_url(data['url'])
        return data
    
    class Meta:
        model = KbsURL
        fields = ('url', 'shortcode')
