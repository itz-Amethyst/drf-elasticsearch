from rest_framework import viewsets
from song.models.music import Music
from song.serializers import  MusicSerializer
class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()