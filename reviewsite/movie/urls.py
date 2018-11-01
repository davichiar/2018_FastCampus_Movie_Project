# 4. url 등록

from django.urls import path
from .views import search_movie

urlpatterns = [
    path('', search_movie, name="search"),
    path('<str:keyword>', search_movie, name="search-result")
]