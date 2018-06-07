from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Book, MyUser
from django.core.files.storage import FileSystemStorage
from pprint import pprint
import requests
import json
from .text import *


class UserFormView(View):
    form_class = RegisterForm
    template_name = 'books/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('books:user-index')

        return render(request, self.template_name, {'form': form})


def user_index(request):
    curr_user = request.user

    if curr_user.is_active:
        print(curr_user.books.all())
        return render(request, 'books/user_index.html', {'all_books': curr_user.books.all, "curr_user": True})
    else:
        return redirect('books:login')

def add_book(request):
    curr_user = request.user

    if curr_user.is_active:
        if request.method == "POST":
            book_title = request.POST.get('book_title', '')
            book_author = request.POST.get('book_author', '')

            try:
                book_cover = request.FILES['book_cover']
            except():
                book_cover = False

            try:
                book_file_ = request.FILES['book_file']
                fs = FileSystemStorage()
                book_file = fs.save(book_file_.name, book_file_)
            except():
                book_file = False

            if not book_title:
                return render(request, 'books/book_form.html', {"not_completed": "not_completed"})

            book_1 = curr_user.books.create(book_title=book_title, book_author=book_author, book_cover=book_cover,
                                            book_file=book_file)
            book_1.save()
            curr_user.save()
            book_content = book_1.book_file.read()
            book_1.book_content = book_content

            words_list, known_words, unknown_words, outside_words = extract_words(request, book_content)

            end = int(len(words_list.split(',')) / 5)
            sugested_words_ = words_list.split()
            sugested_words = []
            for word in sugested_words_:
                if word in unknown_words.split():
                    sugested_words.append(word)

            sugested_words_str = ''
            for word in sugested_words[:end]:
                sugested_words_str += word + ' '

            book_1.all_words = words_list
            book_1.known_words = known_words
            book_1.unknown_words = unknown_words
            book_1.sugested_words = sugested_words_str
            book_1.outside_words = outside_words
            book_1.save()
            return render(request, 'books/user_index.html', {'all_books': curr_user.books.all, "curr_user": True})

        else:
            if request.user.is_active:
                return render(request, 'books/book_form.html')
            else:
                return redirect('books:login')

    if curr_user.is_active:
        return render(request, 'books/user_index.html', {'all_books': curr_user.books.all()})
    return redirect('books:login')


def add_known_words(request):
    curr_user = request.user

    if curr_user.is_active:
        if request.method == "POST":

            try:
                book_file_ = request.FILES['book_file']
                fs = FileSystemStorage()
                book_file = fs.save(book_file_.name, book_file_)
            except():
                book_file = False

            curr_user.known_words_file = book_file
            curr_user.save()
            book_content = curr_user.known_words_file.read()

            known_words = extract_known_words(book_content)
            # curr_user.known_words = known_words
            # curr_user.save()

            for book in curr_user.books.all():
                curr_known_words = str(book.known_words).split()
                curr_unknown_words = str(book.unknown_words).split()
                curr_sugested_words = str(book.sugested_words).split()
                new_known_words = known_words.split()
                a = len(curr_known_words)
                for word in new_known_words:
                    if word not in curr_known_words:
                        curr_known_words.append(word)
                    if word in curr_unknown_words:
                        curr_unknown_words.remove(word)
                    if word in curr_sugested_words:
                        curr_sugested_words.remove(word)

                known_words = ''
                unknown_words = ''
                sugested_words = ''
                for word in curr_known_words:
                    known_words += word + ' '
                book.known_words = known_words

                for word in curr_unknown_words:
                    unknown_words += word + ' '
                book.unknown_words = unknown_words

                for word in curr_sugested_words:
                    sugested_words += word + ' '
                book.sugested_words = sugested_words

                book.save()
                curr_user.known_words = known_words
                curr_user.save()
            curr_user.save()

            return render(request, 'books/user_index.html', {'all_books': curr_user.books.all, "curr_user": True})

        else:
            if request.user.is_active:
                return render(request, 'books/add_known_words.html')
            else:
                return redirect('books:login')

    if curr_user.is_active:
        return render(request, 'books/user_index.html', {'all_books': curr_user.books.all()})
    return redirect('books:login')


def word_meaning(request, word):
    curr_user = request.user
    try:
        meaning_of_word = curr_user.meaning_dict[word]
        return meaning_of_word
    except:
        pass
    app_id = '17160844'
    app_key = '55f44d4c774f7e52ebffd1b8be3e73e9'
    language = 'en'
    #word = 'Ace'
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower() + '/' + 'definitions'
    try:
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        meaning_of_word = json.dumps(r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
        curr_user.meaning_dict[word] = meaning_of_word
    except:
        meaning_of_word = "UNKNOWN WORD"
    return meaning_of_word


#def word_list_meaning(a_word_list):
#    word_dict = dict()
#    request = "hey"
#    for word in a_word_list:
#        word_dict[word] = word_meaning(request,word)
#    return word_dict


def book_details(request, book_id):
    curr_user = request.user
    curr_book = Book.objects.get(pk=book_id)
    book_content = curr_book.book_file.read().decode('utf-8')
    known_words = str(curr_book.known_words).split()
    unknown_words = str(curr_book.unknown_words).split()
    sugested_words = str(curr_book.sugested_words).split()
    red_color = "red"
    black_color = "black"
    book_content = [(word, word_meaning(request, word), red_color) if word in unknown_words else(word, "", black_color) for
                    word in book_content.split()]

    return render(request, 'books/book_details.html', {'book': curr_book,
                                                       'user': curr_user,
                                                       'book_content': book_content,
                                                       'known_words': known_words,
                                                       'unknown_words': unknown_words,
                                                       'sugested_words': sugested_words})
