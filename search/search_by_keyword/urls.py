from django.urls import path
from .views import SearchByKeywordView

urlpatterns = [
    path('search/', SearchByKeywordView.as_view())
]