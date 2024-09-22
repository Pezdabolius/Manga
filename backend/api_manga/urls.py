from django.urls import path
from . import views

urlpatterns = [
    path('api/manga/', views.manga_list, name='manga_list'),
    path('api/manga/<pk>/', views.manga_detail, name='manga_detail'),

    path('api/trs', views.trs_list, name='trs_list'),
    path('api/aap', views.aap_list, name='aap_list'),
    path('api/trg', views.trg_list, name='trg_list'),

    path('api/authors/<pk>/', views.AuthorAPI.as_view(), name='author_detail'),
    path('api/artists/<pk>/', views.ArtistAPI.as_view()),
    path('api/publishers/<pk>/', views.PublisherAPI.as_view()),

    path('api/chapter/<pk>/', views.chapter_detail, name='chapter'),
]