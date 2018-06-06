from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.user_index, name='user-index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'add-book/$', views.add_book, name="add-book"),
    url(r'add-known-words/$', views.add_known_words, name="add-known-words"),
    url(r'(?P<book_id>[0-9]+)/book-details/$', views.book_details, name="book-details"),
]
