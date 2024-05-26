from elasticsearch_dsl import Q

from core.api.elastic.main import PaginatedElasticSearchAPIView
from song.documents.genre import GenreDocument
from song.serializers import GenreSerializer


class SearchGenre(PaginatedElasticSearchAPIView):
    serializer_class = GenreSerializer
    document_class = GenreDocument

    def generate_q_expression(self, query):
        return Q(
                "multi_match", query=query,
                fields=[
                    "name",
                    "description",
                ], fuzziness="auto")
