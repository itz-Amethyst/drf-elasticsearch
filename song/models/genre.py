from django.db import models
from core.models import CoreModel


class Genre(CoreModel):
    
    name = models.CharField(unique=True, blank=False, max_length=255)
    description = models.TextField(blank=True, max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Genras"


    def __str__(self) -> str:
        return f"{self.name}"