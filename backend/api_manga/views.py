from django.shortcuts import render
from rest_framework.response import Response
from .models import Author, Artist, Publisher, \
    Tags, Genre, Release, Manga
from .serializers import MangaSerializer, AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def manga_list(request):
    if request.method == 'GET':
        data = Manga.objects.all()
        serializer = MangaSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MangaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def manga_detail(request, pk):
    try:
        manga = Manga.objects.get(pk=pk)
    except Manga.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MangaSerializer(manga)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MangaSerializer(manga, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        manga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

