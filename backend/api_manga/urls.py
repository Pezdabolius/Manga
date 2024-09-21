from django.urls import path
from . import views

urlpatterns = [
    path('api/manga/', views.manga_list, name='manga_list'),
    path('api/manga/<pk>/', views.manga_detail, name='manga_detail'),
    path('api/types/', views.TypeAPI.as_view()),
    path('api/status/', views.StatusAPI.as_view()),
    path('api/rating/', views.RatingAPI.as_view()),

    path('api/authors/', views.AuthorAPI.as_view(), name='author_list'),
    path('api/authors/<pk>/', views.AuthorAPI.as_view(), name='author_detail'),

    path('api/artists/', views.ArtistAPI.as_view()),
    path('api/artists/<pk>/', views.ArtistAPI.as_view()),

    path('api/publishers/', views.PublisherAPI.as_view()),
    path('api/publishers/<pk>/', views.PublisherAPI.as_view()),

    path('api/tags/', views.TagAPI.as_view(), name='tags'),
    path('api/genres/', views.GenreAPI.as_view()),
    path('api/release/', views.ReleaseAPI.as_view()),

    path('api/chapter/<pk>/', views.chapter_detail, name='chapter'),
]