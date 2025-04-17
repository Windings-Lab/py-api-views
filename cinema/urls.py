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
router.register(r"cinema/cinema_halls", CinemaHallViewSet)
router.register(r"cinema/movies", MovieViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/cinema/genres/", GenreListCreateView.as_view(), name="genre-list"),
    path("api/cinema/genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("api/cinema/actors/", ActorListCreateView.as_view(), name="actor-list"),
    path("api/cinema/actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
]
