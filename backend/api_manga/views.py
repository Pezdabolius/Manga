from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author, Artist, Publisher, \
    Tag, Genre, Release, Manga, Chapter
from .serializers import MangaSerializer, AuthorSerializer, ArtistSerializer, \
    PublisherSerializer, ChapterSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filter import MangaFilter


class CommonDetailAPIView(APIView):
    queryset = None
    serializer_class = None

    def get(self, request, pk):
        queryset = self.queryset.objects.get(pk=pk)
        manga = Manga.objects.filter(Q(author=queryset.id)|
                                     Q(artist=queryset.id)|
                                     Q(publisher=queryset.id)).all()
        manga_serializer = MangaSerializer(manga, many=True)
        serializer = self.serializer_class(queryset)
        manga_list = [
            {
                'title': item['title'],
                'status': item['status'],
                'cover': item['cover']
            } for item in manga_serializer.data
        ]
        response_data = {'name': serializer.data['name'],
                         'description': serializer.data['description'],
                         'manga_list': manga_list
                         }
        return Response(response_data)

    def put(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def trs_list(request):
    if request.method == 'GET':
        response_data = {
            'type': [label for code, label in Manga.MANGA_TYPE],
            'rating': [label for code, label in Manga.RATED],
            'status': [label for code, label in Manga.STATUS]
        }
        return Response(response_data)


@api_view(['GET', 'POST'])
def aap_list(request):
    if request.method == 'GET':
        response_data = {'author': [author for author in Author.objects.values_list('name', flat=True)],
                         'artist': [artist for artist in Artist.objects.values_list('name', flat=True)],
                         'publisher': [artist for artist in Publisher.objects.values_list('name', flat=True)]}
        return Response(response_data)
    elif request.method == 'POST':
        data = request.data
        response_data = {}
        models = {
            'author': Author,
            'artist': Artist,
            'publisher': Publisher,
        }
        for key, model in models.items():
            if key in data:
                name = data[key]
                model = model.objects.create(name=name)
                response_data[key] = {model.name}
                return Response(response_data, status=status.HTTP_201_CREATED)


class AuthorAPI(CommonDetailAPIView):
    queryset = Author
    serializer_class = AuthorSerializer


class ArtistAPI(CommonDetailAPIView):
    queryset = Artist
    serializer_class = ArtistSerializer


class PublisherAPI(CommonDetailAPIView):
    queryset = Publisher
    serializer_class = PublisherSerializer


@api_view(['GET', 'POST'])
def trg_list(request):
    if request.method == 'GET':
        response_data = {'tag': [tag for tag in Tag.objects.values_list('name', flat=True)],
                         'release': [release for release in Release.objects.values_list('name', flat=True)],
                         'genre': [genre for genre in Genre.objects.values_list('name', flat=True)]}
        return Response(response_data)
    if request.method == 'POST':
        data = request.data
        response_data = {}
        models = {
            'tag': Tag,
            'release': Release,
            'genre': Genre,
        }
        for key, model in models.items():
            if key in data:
                name = data[key]
                model = model.objects.create(name=name)
                response_data[key] = {model.name}
                return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def manga_list(request):
    if request.method == 'GET':
        data = Manga.objects.all()
        filtered_data = MangaFilter(request.GET, queryset=data).qs
        serializer = MangaSerializer(filtered_data, many=True)
        response_data = [
            {
                'title': item['title'],
                'cover': item['cover'],
                'type': item['type']
            } for item in serializer.data
        ]
        return Response(response_data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MangaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def manga_detail(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    if request.method == 'GET':
        chapter = Chapter.objects.filter(manga=manga).all()
        chapter_serializer = ChapterSerializer(chapter, many=True)
        chapters = [
            {
                'volume': item['volume'],
                'chapter': item['chapter'],
                'title': item['title'],
                'user': item['user']
            } for item in chapter_serializer.data
        ]
        serializer = MangaSerializer(manga)
        response_data = {
            **serializer.data,
            'chapters': chapters,
        }
        return Response(response_data)
    elif request.method == 'PUT':
        serializer = MangaSerializer(manga, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        manga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    if request.method == 'GET':
        images = chapter.extract_images()
        serializer = ChapterSerializer(chapter)
        response_data = {
            **serializer.data,
            'images': images
        }
        return Response(response_data)
    elif request.method == 'POST' or request.method == 'PUT':
        serializer = ChapterSerializer(chapter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.method == 'POST':
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)