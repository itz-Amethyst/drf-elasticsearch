from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from song.models.genre import Genre

@registry.register_document
class GenreDocument(Document):
    id = fields.IntegerField()
    class Index:
        name = "genres"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        model = Genre
        fields = [
            "name",
            "description"
        ]