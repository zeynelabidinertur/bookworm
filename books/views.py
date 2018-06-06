from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Book
from django.core.files.storage import FileSystemStorage
from pprint import pprint
import requests
import json

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
                book_file = request.FILES['book_file']
                print (book_file)
                fs = FileSystemStorage()
                book_file = fs.save(book_file.name, book_file)
            except():
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

def word_meaning(word):
    app_id = '17160844'
    app_key = '55f44d4c774f7e52ebffd1b8be3e73e9'
    language = 'en'
    #word = 'Ace'
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower() + '/' + 'definitions'
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    print(
    "json \n" + json.dumps(r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]))

    meaning_of_word = json.dumps(r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
    return meaning_of_word

def word_list_meaning(a_word_list):
    word_dict = dict()
    for word in a_word_list:
        try:
            word_dict[word] = word_meaning(word)
        except:
            word_dict[word] = "UNKNOWN WORD"
    return word_dict




def book_details(request, book_id):
    curr_user = request.user
    curr_book = Book.objects.get(pk=book_id)
    book_content = curr_book.book_file.read().decode('utf-8')
    a_dict = {"DIPLOBLASTIC": "Characterizing the ovum when it has two primary germinallayers.",
              "DEFIGURE": "To delineate. [Obs.]These two stones as they are here defigured. Weever.",
              "LOMBARD": "Of or pertaining to Lombardy, or the inhabitants of Lombardy.",
              "BAHAISM": "The religious tenets or practices of the Bahais.",
              "FUMERELL": "See Femerell.",
              "ROYALET": "A petty or powerless king. [R.]there were at this time two other royalets, as only kings by hisleave. Fuller.",
              "TROPHIED": "Adorned with trophies.The trophied arches, storied halls, invade. Pope.",
              "ZEQUIN": "See Sequin.",
              "MILLWRIGHT": "A mechanic whose occupation is to build mills, or to set uptheir machinery.",
              "PHOTOGRAPHOMETER": "An instrument for determining the senluminous rays.",
              "SCHEELIUM": "The metal tungsten. [Obs.]",
              "ALVEOLATE": "Deeply pitted, like a honeycomb.",
              "LIMULUS": "The only existing geno Molucca crab, king crab,horseshoe crab, and horsefoot.",
              "OSMUND": "A fern of the genus O (Osmuronds, ofteas been used in stiffening linen.",
              "POTTEEN": "See Poteen.",
              "UNDERRUN": "To run or pass undein, or of examiningit.",
              "EMPLASTIC": "Fit to be applied as a plaster; glutinous; adhesive; as,emplastic applications.",
              "RHYTHMICS": "The department of musical science which treats of the length ofsounds.",
              "PLEUROPTERA": "A group of Isectivora, including the colugo.",
              "UNBLOODY": "Not bloody. Dryden. Unbloody sacrifice. (a) A she Mass.",
              "CINCINNUS": "A form of monochasium in which the lateral branche false axis; -- called alsoscoal (#), a.",
              "INDOCILITY": "The quality or state of beiness.The stiffness and indocility of the Pharisees. W. Montagu.",
              "TELEOCEPHIAL": "An extensive order ood, perch, etc.",
              "CANEBRAKE": "A thicket of canes. Ellicott.",
              "QUININIC": "Pertaining to, or designating, a nitrogeny the oxidation of quinine.",
              "RICINIC": "Pertaining to, or derived from, castor oil; formerly,designating an acid now called ricinoleic acid.",
              "TELLURAL": "Of or pertaining to the earth. [R.]",
              "OTHERNESS": "The quality or state of being other or different; alterity;oppositeness.",
              "FASCICLE": "A small bundle or collection; a compact cluster; as, a fascicleof fibers; a fascicle of flowers or roots.",
              "REENJOYMENT": "Renewed enjoiment.",
              "LONGIROSTER": "One of the Longirostres.",
              "RHAPSODIZE": "To utter as a rhapsody, or in the manner of a rhapsody Sterne.",
              "WATER VIOLET": "See under Violet.",
              "TRUNCHEONED": "Having a truncheon.",
              "UNDERWENT": "imp. of Undergo.",
              "APITPAT": "With quick beating or palpitation; pitapat. Congreve.",
              "MISTITLE": "To call by a wrong title.",
              "PERSUASIBILITY": "Capability of being persuaded. Hawthorne.",
              "RAFTING": "The business of making or managing rafts.",
              "PROTEROGYNOUS": "Having the pistil come to maturiterandrous.",
              "MULTIFACED": "Having many faces."}
    a_word_list = list(a_dict.keys())
    word_dict = a_dict
    #word_dict = word_list_meaning(a_word_list)

    return render(request, 'books/book_details.html', {'book': curr_book,
                                                       'user': curr_user,
                                                       'book_content': book_content,
                                                       'word_list': word_dict})
