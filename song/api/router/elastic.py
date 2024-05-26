from django.urls import path

from song.api.elastic.music import SearchMusic
from song.api.elastic.genre import SearchGenre

urlpatterns = [
    path("genre/<str:query>/", SearchGenre.as_view()),
    path("song/<str:query>/", SearchMusic.as_view()),
]