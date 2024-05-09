from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Clothe, Type
from .serializers import ClotheSerializer

class ClotheViewSet(viewsets.ModelViewSet):
    queryset = Clothe.objects.all()
    serializer_class = ClotheSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SearchClotheView(APIView):
    def get(self, request):
        keyword = request.query_params.get('keyword', '')

        clothes = Clothe.objects.filter(
            Q(name__icontains=keyword) |
            Q(type__name__icontains=keyword)
        ).distinct()

        serializer = ClotheSerializer(clothes, many=True)
        return Response(serializer.data)

