from rest_framework import serializers
from .models import Author, Artist, Publisher, \
    Tags, Genre, Release, Manga


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'description']


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'description']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'description']


class MangaSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(slug_field='name', read_only=True)
    artist = serializers.SlugRelatedField(slug_field='name', read_only=True)
    publisher = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    releases = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    type = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    class Meta:
        model = Manga
        fields = '__all__'

    def get_type(self, obj):
        return obj.get_type_display()

    def get_status(self, obj):
        return obj.get_status_display()