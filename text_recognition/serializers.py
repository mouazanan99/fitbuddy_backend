from rest_framework import serializers
from .models import Response

# Response Serializer
class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = (
            'question',
              )