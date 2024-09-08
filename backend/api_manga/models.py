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


class Tags(CommonInfo):
    pass


class Release(CommonInfo):
    pass


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
    cover = models.ImageField(upload_to='covers/', blank=True)
    background = models.ImageField(upload_to='backgrounds/', blank=True)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    releases = models.ManyToManyField(Release)
    type = models.CharField(max_length=2, choices=MANGA_TYPE)
    status = models.CharField(max_length=2, choices=STATUS)
    rating = models.CharField(max_length=5, choices=RATED)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



