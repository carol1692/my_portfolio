from django.urls import path
from reading_diary.views import IndexView, LoginView

urlpatterns = [
    path("", IndexView.as_view(), name="index_reading"),
    path("register_user", LoginView.as_view(), name="register_user"),
]