from rest_framework import serializers

from core.api.serializers import UserSerializer
from song.models import Genre, Music
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MusicSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Music
        fields = "__all__"