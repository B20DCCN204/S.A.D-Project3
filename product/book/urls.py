from django.urls import path
from .views import SearchBookView

urlpatterns = [
    path('search-book/', SearchBookView.as_view())
]