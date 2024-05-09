from rest_framework import serializers
from .models import Clothe, Type

class ClotheSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = Clothe
        fields = ['id', 'name', 'image', 'type', 'brand', 'price', 'quantity']
