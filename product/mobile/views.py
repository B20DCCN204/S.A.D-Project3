from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mobile
from .serializers import MobileSerializer

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SearchMobileView(APIView):
    def get(self, request):
        keyword = request.query_params.get('keyword', '')

        mobiles = Mobile.objects.filter(
            Q(name__icontains=keyword) |
            Q(type__name__icontains=keyword)
        ).distinct()

        serializer = MobileSerializer(mobiles, many=True)
        return Response(serializer.data)