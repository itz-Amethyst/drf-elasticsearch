from rest_framework import viewsets
from song.models.genre import Genre
from song.models.music import Music
from song.serializers import GenreSerializer, MusicSerializer

# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()