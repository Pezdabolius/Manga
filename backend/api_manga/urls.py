from django.urls import path
from . import views

urlpatterns = [
    path('api/manga_list/', views.manga_list),
    path('api/manga_detail/<pk>/', views.manga_detail),
    path('api/author_list/', views.AuthorAPI.as_view()),
    path('api/author_detail/<pk>/', views.AuthorAPI.as_view()),
    path('api/artists_list/', views.ArtistAPI.as_view()),
    path('api/artist_detail/<pk>/', views.ArtistAPI.as_view()),
    path('api/publishers_list/', views.PublisherAPI.as_view()),
    path('api/publisher_detail/<pk>/', views.PublisherAPI.as_view()),
    path('api/tags_list/', views.TagAPI.as_view()),
    path('api/genres_list/', views.GenreAPI.as_view()),
]