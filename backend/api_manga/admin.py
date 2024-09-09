from django.contrib import admin
from .models import Author, Artist, Publisher, \
    Tags, Genre, Release, Manga


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'authors',
                    'publisher', 'type', 'status', 'rating']
    filter_horizontal = ('tags', 'releases')
    search_fields = ['title', 'authors', 'publisher', 'type', 'status']
    list_filter = ['authors', 'publisher', 'type', 'status']
    list_editable = ['status', 'rating', 'type']