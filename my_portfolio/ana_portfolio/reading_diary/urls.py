from django.urls import path
from reading_diary.views import IndexView

urlpatterns = [
    path("", IndexView.as_view())
]