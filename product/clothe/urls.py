from django.urls import path
from .views import SearchClotheView

urlpatterns = [
    path('search-clothe/', SearchClotheView.as_view())
]