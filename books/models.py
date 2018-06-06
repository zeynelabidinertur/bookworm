from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from newWords import settings
fileStorage = FileSystemStorage(location=settings.MEDIA_ROOT)
# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length=250)
    book_author = models.CharField(max_length=250)
    book_file = models.FileField(storage=fileStorage, blank=True, null=True)
    book_cover = models.FileField(storage=fileStorage, blank=True, null=True)
    book_content = models.TextField(blank=True, null=True)
    all_words = models.TextField(blank=True, null=True)
    known_words = models.TextField(blank=True, null=True)
    unknown_words = models.TextField(blank=True, null=True)
    outside_words = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.book_title


class MyUser(AbstractUser):
    books = models.ManyToManyField(Book, blank=True, null=True)

