from rest_framework import serializers
from .models import Mobile, Type

class MobileSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = Mobile
        fields = ['id', 'name', 'image', 'type', 'producer', 'price', 'quantity']
