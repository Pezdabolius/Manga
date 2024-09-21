from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tag, Author, Publisher, Artist, Manga, \
    Genre


class TRGTest(APITestCase):
    model = Tag
    url = 'tags'
    data = {
        'name': 'Cold Weapons'
    }

    def get_url(self):
        return reverse(self.url)

    def test_trg_list(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_trg_post(self):
        response = self.client.post(self.get_url(), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Tag.objects.filter(name=self.data['name']).exists())


class AAPTest(APITestCase):
    model = Author
    url_list = 'author_list'
    url_detail = 'author_detail'
    data = {'name': 'Yukinobu Tatsu',
            'description': 'To start, Tatsu was asked about the "detail" that '
                           'went into the drawings of the manga'
            }

    def get_url(self, url, *args):
        return reverse(url, args=args)

    def setUp(self):
        self.author = Author.objects.create(**self.data)

    def test_app_list(self):
        response = self.client.get(self.get_url(self.url_list))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_app_post(self):
        response = self.client.post(self.get_url(self.url_list), data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Author.objects.filter(description=self.data['description']).exists())