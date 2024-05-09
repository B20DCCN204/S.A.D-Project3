from django.urls import path
from .views import CartView, AddToCartView

urlpatterns = [
    path('carts/<int:pk>', CartView.as_view(), name='cart-detail'),
    path('add-to-cart/', AddToCartView.as_view())
]
