from core.api.elastic.main import PaginatedElasticSearchAPIView
from core.api.serializers import UserSerializer
from core.documents.user import UserDocument
from elasticsearch_dsl import Q


class SearchUsers(PaginatedElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q("bool",
                 should=[
                     Q("match", username=query),
                     Q("match", first_name=query),
                     Q("match", last_name=query),
                 ], minimum_should_match=1)