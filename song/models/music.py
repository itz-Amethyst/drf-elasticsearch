from django.db import models
from django.conf import settings
from core.models import CoreModel
from song.models.genre import Genre

class Music(CoreModel):
    
    title = models.CharField(blank=False, max_length=255)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=255, null=True)
    genres = models.ManyToManyField(to=Genre, blank=False, related_name="genres")
    first_release = models.IntegerField()


    def __str__(self):
        return f"{self.author}: {self.title} ({self.created_at.date()})"