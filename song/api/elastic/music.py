from elasticsearch_dsl import Q

from core.api.elastic.main import PaginatedElasticSearchAPIView
from song.serializers import MusicSerializer


class SearchMusic(PaginatedElasticSearchAPIView):
    serializer_class = MusicSerializer
    document_class = MusicSerializer

    def generate_q_expression(self, query):
        return Q(
                "multi_match", query=query,
                fields=[
                    "title",
                    "author",
                    "first_release"
                ], fuzziness="auto")