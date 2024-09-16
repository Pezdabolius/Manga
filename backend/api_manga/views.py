from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author, Artist, Publisher, \
    Tag, Genre, Release, Manga, Chapter
from .serializers import MangaSerializer, AuthorSerializer, ArtistSerializer, \
    PublisherSerializer, TagSerializer, GenreSerializer, ReleaseSerializer, \
    ChapterSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filter import MangaFilter


class CommonListAPIView(APIView):
    queryset = None
    serializer_class = None

    def get(self, request):
        serializer = self.serializer_class(self.queryset.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class TypeAPI(APIView):
    def get(self, request):
        return Response([{'type': label} for code, label in Manga.MANGA_TYPE])


class RatingAPI(APIView):
    def get(self, request):
        return Response([{'rating': label} for code, label in Manga.RATED])


class StatusAPI(APIView):
    def get(self, request):
        return Response([{'status': label} for code, label in Manga.STATUS])


class AuthorAPI(CommonListAPIView, CommonDetailAPIView):
    queryset = Author
    serializer_class = AuthorSerializer

    def get(self, request, pk=None):
        if pk is None:
            return CommonListAPIView.get(self, request)
        else:
            return CommonDetailAPIView.get(self, request, pk)


class ArtistAPI(CommonListAPIView, CommonDetailAPIView):
    queryset = Artist
    serializer_class = ArtistSerializer

    def get(self, request, pk=None):
        if pk is None:
            return CommonListAPIView.get(self, request)
        else:
            return CommonDetailAPIView.get(self, request, pk)


class PublisherAPI(CommonListAPIView, CommonDetailAPIView):
    queryset = Publisher
    serializer_class = PublisherSerializer

    def get(self, request, pk=None):
        if pk is None:
            return CommonListAPIView.get(self, request)
        else:
            return CommonDetailAPIView.get(self, request, pk)


class TagAPI(CommonListAPIView):
    queryset = Tag
    serializer_class = TagSerializer


class GenreAPI(CommonListAPIView):
    queryset = Genre
    serializer_class = GenreSerializer


class ReleaseAPI(CommonListAPIView):
    queryset = Release
    serializer_class = ReleaseSerializer


@api_view(['GET', 'POST'])
def manga_list(request):
    if request.method == 'GET':
        data = Manga.objects.all()
        filtered_data = MangaFilter(request.GET, queryset=data).qs
        serializer = MangaSerializer(filtered_data, many=True)
        return Response(serializer.data)
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