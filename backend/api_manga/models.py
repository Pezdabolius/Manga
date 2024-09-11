from django.db import models


class CommonForPeople(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1500, blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(CommonForPeople):
    pass


class Artist(CommonForPeople):
    pass


class Publisher(CommonForPeople):
    pass


class CommonInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(CommonInfo):
    pass


class Tag(CommonInfo):
    pass


class Release(CommonInfo):
    pass


def dynamic_cover_upload_to(instance, filename):
    filename = f'{instance.title}.jpg'
    return f'covers/{filename}'


def dynamic_background_upload_to(instance, filename):
    filename = f'Back_for_{instance.title}.jpg'
    return f'backgrounds/{filename}'


class Manga(models.Model):
    MANGA_TYPE = [
        ('MG', 'Manga'),
        ('OE', 'OEL-manga'),
        ('MH', 'Manhwa'),
        ('MU', 'Manhua'),
        ('CM', 'Comic'),
    ]
    STATUS = [
        ('ON', 'Ongoing'),
        ('CO', 'Completed'),
        ('AN', 'Announcement'),
        ('DI', 'Discontinued'),
    ]
    RATED = [
        ('PG-13', 'PG-13'),
        ('R', 'Restricted'),
        ('NC-17', 'NC-17'),
    ]
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1500)
    cover = models.ImageField(upload_to=dynamic_cover_upload_to, blank=True)
    background = models.ImageField(upload_to=dynamic_background_upload_to, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=None)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    genre = models.ManyToManyField(Genre)
    release = models.ManyToManyField(Release, blank=True)
    type = models.CharField(max_length=2, choices=MANGA_TYPE)
    status = models.CharField(max_length=2, choices=STATUS)
    rating = models.CharField(max_length=5, choices=RATED)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



