from django.urls import path , include
from rest_framework import routers
from song.views import GenreViewSet, MusicViewSet

router = routers.DefaultRouter()
router.register(r"genre", GenreViewSet)
router.register(r"music", MusicViewSet)


urlpatterns = [
    path("", include(router.urls)),
]