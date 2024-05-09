from rest_framework import serializers
from .models import Book, Category, Author, Publisher


class BookSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )
    authors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "image",
            "authors",
            "publisher",
            "categories",
            "price",
            "quantity",
        ]

