from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreListCreateView,
    GenreDetailView,
    ActorListCreateView,
    ActorDetailView,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register(r"cinema/movies", MovieViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "api/cinema/genres/",
        GenreListCreateView.as_view(),
        name="genre-list"
    ),
    path(
        "api/cinema/genres/<int:pk>/",
        GenreDetailView.as_view(),
        name="genre-detail"
    ),
    path(
        "api/cinema/actors/",
        ActorListCreateView.as_view(),
        name="actor-list"
    ),
    path(
        "api/cinema/actors/<int:pk>/",
        ActorDetailView.as_view(),
        name="actor-detail"
    ),
    path(
        "api/cinema/cinema_halls/",
        CinemaHallViewSet.as_view({"get": "list", "post": "create"}),
        name="cinema-hall-list",
    ),
    path(
        "api/cinema/cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }),
        name="cinema-hall-detail",
    ),
]
