import requests
from django.shortcuts import render
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart
from .serializers import CartSerializer


class CartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AddToCartView(APIView):

    def post(self, request):
        user_id = self.get_user_info(request).get('id')
        product_type = request.data.get('product_type')
        product_id = request.data.get('product_id')
        price = self.get_price_for_product(product_type, product_id)

        cart_data = {
            'user_id': user_id,
            'product_type': product_type,
            'product_id': product_id,
            'quantity': request.data.get('quantity'),
        }

        serializer = CartSerializer(data=cart_data, context={'price': price})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_user_info(self, request):
        token = request.data.get('token')
        response = requests.get('http://127.0.0.1:8001/user/api/user-info/', headers={'Authorization': f'Bearer {token}'})
        return response.json()
    def get_price_for_product(self, product_type, product_id):
        if product_type == 'book':
            response = requests.get(f'http://127.0.0.1:8002/product/api/books/{product_id}')
            price = response.json().get('price', 0)
        elif product_type == 'mobile':
            response = requests.get(f'http://127.0.0.1:8002/product/api/mobiles/{product_id}')
            price = response.json().get('price', 0)
        elif product_type == 'clothe':
            response = requests.get(f'http://127.0.0.1:8002/product/api/clothes/{product_id}')
            price = response.json().get('price', 0)
        else:
            price = 0
        return price

