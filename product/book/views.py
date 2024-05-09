from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Category, Author, Publisher
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SearchBookView(APIView):
    def get(self, request):
        keyword = request.query_params.get('keyword', '')

        books = Book.objects.filter(
            Q(title__icontains=keyword) |
            Q(categories__name__icontains=keyword) |
            Q(authors__name__icontains=keyword) |
            Q(publisher__name__icontains=keyword)
        ).distinct()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)