from django.urls import path
from .views import RegisterView, LoginView, UserInfoView, LogoutView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("user-info/", UserInfoView.as_view()),
    path("logout/", LogoutView.as_view()),
]
