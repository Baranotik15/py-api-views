from django.urls import path, include
from rest_framework import  routers
from cinema.views import (
    movie_list,
    movie_detail,
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
)


app_name = "cinema"
router = routers.DefaultRouter()

router.register("actor", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genre", GenreViewSet)

urlpatterns = [
    path("movies/", movie_list),
    path("movies/<int:pk>/", movie_detail),
    path("actors/", ActorList.as_view(), name='actor-list'),
    path("actors/<int:pk>/", ActorDetail.as_view(), name='actor-detail'),
    path("genres/", GenreList.as_view(), name='genre-list'),
    path("genres/<int:pk>/", GenreDetail.as_view(), name='genre-detail'),
    path("", include(router.urls)),
]
