from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Book
from django.core.files.storage import FileSystemStorage

# Create your views here.


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
        print (curr_user.books.all())
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
            except:
                book_cover = False

            try:
                book_file = request.FILES['book_file']
                fs = FileSystemStorage()
                book_file = fs.save(book_file.name, book_file)
            except:
                book_file = False

            if not book_title:
                return render(request, 'books/book_form.html', {"not_completed": "not_completed"})
            #if book_cover:
             #   fs = FileSystemStorage()
              #  filename = fs.save(book_cover.name, book_cover)
            #else:
             #   filename = '..\media\default_book_cover_logo.jpg'

            book_1 = curr_user.books.create(book_title=book_title, book_author=book_author,
                                                book_cover=book_cover, book_file = book_file)
            book_1.save()
            curr_user.save()
            return render(request, 'books/user_index.html', {'all_books': curr_user.books.all, "curr_user": True})

        else:
            if request.user.is_active:
                return render(request, 'books/book_form.html')
            else:
                return redirect('books:login')

    if curr_user.is_active:
        return render(request, 'books/user_index.html', {'all_books': curr_user.books.all()})
    return redirect('books:login')


def book_details(request, book_id):
    curr_user = request.user
    curr_book = Book.objects.get(pk=book_id)
    book_content = curr_book.book_file.read()

    return render(request, 'books/book_details.html', {'book_content': book_content})