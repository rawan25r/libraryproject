from django.http import HttpResponse
from django.shortcuts import render

# ====== دوال اللاب القديم (ما حذفتها) ======
def index_old(request):

    name = request.GET.get("name", "world!")
    return HttpResponse(f"Hello, {name}")

def index2(request, val1):
    return HttpResponse(f"value1 = {val1}")

def viewbook(request, bookId):
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

def links_page(request):
    return render(request, 'books/links.html')

def listing_page(request):
    return render(request, 'books/listing.html')


def tables_page(request):
    return render(request, 'books/tables.html')

def text_formatting_page(request):
    return render(request, 'books/text_formatting.html')


def index3(request, val1, val2):
    return HttpResponse(f"val1 = {val1}, val2 = {val2}")


# ====== دوال اللاب الجديد (HTML + CSS + Templates) ======
# ملاحظة: لازم تكون أسماء الدوال مطابقة لأسماء الروابط في urls.py

def index(request):
    return render(request, 'bookmodule/index.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def view_one_book(request, book_id):
    return render(request, 'bookmodule/one_book.html', {"book_id": book_id})
