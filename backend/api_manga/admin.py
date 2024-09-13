from django.contrib import admin
from .models import Author, Artist, Publisher, \
    Tag, Genre, Release, Manga, Chapter


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


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author',
                    'publisher', 'type', 'status', 'rating']
    filter_horizontal = ('genre','tag', 'release')
    search_fields = ['title', 'author', 'publisher', 'type', 'status']
    list_filter = ['author', 'publisher', 'type', 'status']
    list_editable = ['status', 'rating', 'type']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['manga', 'volume', 'chapter', 'title']
    list_filter = ['manga', 'volume']