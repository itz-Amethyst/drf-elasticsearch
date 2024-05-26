from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from song.models.music import Music

@registry.register_document
class SongDocument(Document):
    author = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "first_name": fields.TextField(),
        "last_name": fields.TextField(),
        "username": fields.TextField(),
    })
    genres = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "name": fields.TextField(),
        "description": fields.TextField(),
    })

    class Index:
        name = "songs"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Music
        fields = [
            "title",
            "description",
            "first_release",
            "created_at",
            "modified_at",
        ]