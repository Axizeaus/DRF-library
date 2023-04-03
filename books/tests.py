from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title = 'test title',
            subtitle = 'test subtitle',
            author = 'test author',
            isbn = '0000000000000'
        )
        
    def test_book_content(self):
        self.assertEqual(self.book.title, 'test title')
        self.assertEqual(self.book.author, 'test author')
        self.assertEqual(self.book.subtitle, 'test subtitle')
        self.assertEqual(self.book.isbn, '0000000000000')
        
    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'test subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')