from django.contrib import admin

from .models import MyUser, Book
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Book)