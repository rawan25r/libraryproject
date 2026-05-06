from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# ============================================================
#                     LAB 10 PART 2 (Django Forms)
# ============================================================

def list_books_p2(request):
    books = Book.objects.all()
    return render(request, 'books/lab9_part2_list.html', {'books': books})


def add_book_p2(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')

    return render(request, 'books/lab9_part2_add.html', {'form': form})


def edit_book_p2(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')

    return render(request, 'books/lab9_part2_edit.html', {'form': form})


def delete_book_p2(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/books/lab9_part2/listbooks')

# ============================================================
#                     CRUD (LAB 10 PART 1)
# ============================================================

def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/lab9_part1_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            pubdate=request.POST['pubdate'],
            rating=request.POST['rating'],
        )
        return redirect('/books/lab9_part1/listbooks')

    return render(request, 'books/lab9_part1_add.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.price = request.POST['price']
        book.quantity = request.POST['quantity']
        book.pubdate = request.POST['pubdate']
        book.rating = request.POST['rating']
        book.save()

        return redirect('/books/lab9_part1/listbooks')

    return render(request, 'books/lab9_part1_edit.html', {'book': book})


def delete_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/books/lab9_part1/listbooks')


def index(request):
    return HttpResponse("Library Project Home Page")
