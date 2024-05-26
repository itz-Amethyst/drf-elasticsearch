from rest_framework import viewsets
from song.models.genre import Genre
from song.serializers import  GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()