from django.urls import path
from .views import SearchMobileView

urlpatterns = [
    path('search-mobile/', SearchMobileView.as_view())
]