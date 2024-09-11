from rest_framework import serializers
from .models import Author, Artist, Publisher, \
    Tag, Genre, Release, Manga


class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = []


class AuthorSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Author
        fields = ['name', 'description']


class TagSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Tag
        fields = ['name']


class GenreSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Genre
        fields = ['name']


class ReleaseSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Release
        fields = ['name']


class PublisherSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Publisher
        fields = ['name', 'description']


class ArtistSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Artist
        fields = ['name', 'description']


class MangaSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(slug_field='name', read_only=True)
    artist = serializers.SlugRelatedField(slug_field='name', read_only=True)
    publisher = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tag = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genre = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    release = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    type = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Manga
        fields = '__all__'

    def get_type(self, obj):
        return obj.get_type_display()

    def get_status(self, obj):
        return obj.get_status_display()