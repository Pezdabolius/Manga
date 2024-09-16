from django_filters import FilterSet, ChoiceFilter, ModelMultipleChoiceFilter
from .models import Tag, Genre, Release, \
    Manga


class MangaFilter(FilterSet):
    tag = ModelMultipleChoiceFilter(queryset=Tag.objects.all())
    genre = ModelMultipleChoiceFilter(queryset=Genre.objects.all())
    release = ModelMultipleChoiceFilter(queryset=Release.objects.all())
    type = ChoiceFilter(choices=Manga.MANGA_TYPE)
    status = ChoiceFilter(choices=Manga.STATUS)
    rating = ChoiceFilter(choices=Manga.RATED)

    class Meta:
        model = Manga
        fields = ['tag', 'genre', 'release', 'type', 'status', 'rating']
