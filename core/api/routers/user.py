from django.urls import path , include
from rest_framework import routers
from core.api.view.user import UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]