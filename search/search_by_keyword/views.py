import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class SearchByKeywordView(APIView):
    def get(self, request):
        book_results = self.search_book(request.query_params.get('keyword', ''))
        mobile_results = self.search_mobile(request.query_params.get('keyword', ''))
        clothe_results = self.search_clothe(request.query_params.get('keyword', ''))

        results = {
            'books': book_results,
            'mobile': mobile_results,
            'clothe': clothe_results,
        }

        return Response(results)


    def search_book(self, query):
        response = requests.get('http://127.0.0.1:8002/product/search-book/', params={'keyword': query})
        return response.json()

    def search_mobile(self, query):
        response = requests.get('http://127.0.0.1:8002/product/search-mobile/', params={'keyword': query})
        return response.json()

    def search_clothe(self, query):
        response = requests.get('http://127.0.0.1:8002/product/search-clothe/', params={'keyword': query})
        return response.json()