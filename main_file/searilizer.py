from rest_framework import serializers
from .models import URLSTORAGE

class URLserializer(serializers.ModelSerializer):
    custom_code = serializers.CharField(required=False,allow_blank=True)
    expires_at = serializers.DateTimeField(required=False)
    
    class Meta:
        model = URLSTORAGE
        fields = ["original_url","custom_code","expires_at"]

    def validate_original_uri(self,value):
        if not value.statrtswith(("http://","https://")):
            raise serializers.ValidationError('only http/https urls are allowed ')
        return value 
    
    def validate_custom_url(self,value):
        if URLSTORAGE.objects.filter(short_code=value).exists():
            raise serializers.ValidationError("custum code already in user")
        return value
    