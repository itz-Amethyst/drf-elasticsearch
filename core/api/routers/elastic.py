from django.urls import path

from core.api.elastic.user import SearchUsers

urlpatterns = [
    path("user/<str:query>/", SearchUsers.as_view()),
]