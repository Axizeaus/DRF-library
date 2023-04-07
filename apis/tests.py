from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setupTEstData(cls):
        cls.book = Book.objects.create(
            title = 'test title',
            subtitle = 'test subtitle',
            author = 'test author',
            isbn = '0123456789012'
        )
        
    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)