from django.http import HttpResponse
from django.shortcuts import render

# Models
from .models import Book, Address, Student, Publisher, Author

# Django ORM tools
from django.db.models import (
    F, Sum, FloatField, ExpressionWrapper,
    Q, Count, Avg, Max, Min
)

# ============================================================
#                     LAB 9 FUNCTIONS
# ============================================================

from django.utils import timezone
import random

def seed_data(request):
    # Clear old data
    Publisher.objects.all().delete()
    Author.objects.all().delete()
    Book.objects.all().delete()

    # Create publishers
    publishers = []
    for i in range(5):
        p = Publisher.objects.create(
            name=f"Publisher {i+1}",
            location=f"City {i+1}"
        )
        publishers.append(p)

    # Create authors
    authors = []
    for i in range(10):
        a = Author.objects.create(
            name=f"Author {i+1}",
            DOB="1980-01-01"
        )
        authors.append(a)

    # Create books
    for i in range(20):
        b = Book.objects.create(
            title=f"Book {i+1}",
            price=random.randint(10, 200),
            quantity=random.randint(1, 20),
            pubdate=timezone.now(),
            rating=random.randint(1, 5),
            publisher=random.choice(publishers)
        )
        # Add 1–3 authors randomly
        b.authors.add(*random.sample(authors, random.randint(1, 3)))

    return HttpResponse("Seed data created successfully!")


def task1(request):
    books = Book.objects.all()
    return render(request, "lab9/task1.html", {"books": books})

def task2(request):
    students = Student.objects.all()
    return render(request, "lab9/task2.html", {"students": students})

def task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books=Count(
            'book',
            filter=Q(book__price__gt=50, book__quantity__lt=5, book__quantity__gte=1)
        )
    )
    return render(request, 'lab9/task6.html', {'publishers': publishers})


def task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_books=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'lab9/task5.html', {'publishers': publishers})


def task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'lab9/task4.html', {'publishers': publishers})


def task3(request):
    publishers = Publisher.objects.annotate(
        oldest_book=Min('book__pubdate')
    )
    return render(request, 'lab9/task3.html', {'publishers': publishers})


def task2(request):
    publishers = Publisher.objects.annotate(
        total_stock=Sum('book__quantity')
    )
    return render(request, 'lab9/task2.html', {'publishers': publishers})


def task1(request):
    total_books = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1

    books = Book.objects.annotate(
        availability=ExpressionWrapper(
            (F('quantity') * 100.0) / total_books,
            output_field=FloatField()
        )
    )

    return render(request, 'lab9/task1.html', {'books': books})


# ============================================================
#                     SEED DATA (LAB 8 + LAB 9)
# ============================================================

def seed_all_data(request):

    # LAB 8 DATA (unchanged)
    riyadh = Address.objects.create(city="Riyadh")
    jeddah = Address.objects.create(city="Jeddah")
    dammam = Address.objects.create(city="Dammam")
    mecca = Address.objects.create(city="Mecca")
    medina = Address.objects.create(city="Medina")

    Book.objects.create(title="Django for Beginners", author="Ali Ahmed", price=60, edition=1, pubdate="2020-01-01")
    Book.objects.create(title="Advanced Django", author="Sara Khalid", price=150, edition=4, pubdate="2020-01-01")
    Book.objects.create(title="Python Quick Guide", author="Mohammed Saleh", price=70, edition=2, pubdate="2020-01-01")
    Book.objects.create(title="Quality Software", author="Noura Hassan", price=95, edition=5, pubdate="2020-01-01")
    Book.objects.create(title="Data Structures", author="Fahad Omar", price=80, edition=3, pubdate="2020-01-01")
    Book.objects.create(title="Machine Learning", author="Aisha Abdullah", price=200, edition=6, pubdate="2020-01-01")
    Book.objects.create(title="SQL Mastery", author="Lama Youssef", price=55, edition=1, pubdate="2020-01-01")

    Student.objects.create(name="Aisha", age=20, address=riyadh)
    Student.objects.create(name="Fahad", age=22, address=jeddah)
    Student.objects.create(name="Lama", age=19, address=riyadh)
    Student.objects.create(name="Omar", age=23, address=dammam)
    Student.objects.create(name="Noura", age=21, address=mecca)
    Student.objects.create(name="Salem", age=24, address=medina)
    Student.objects.create(name="Reem", age=20, address=jeddah)

    # LAB 9 DATA (added)
    p1 = Publisher.objects.create(name="O'Reilly Media", location="USA")
    p2 = Publisher.objects.create(name="Packt Publishing", location="UK")
    p3 = Publisher.objects.create(name="No Starch Press", location="USA")

    a1 = Author.objects.create(name="Ali Ahmed", DOB="1980-05-10")
    a2 = Author.objects.create(name="Sara Khalid", DOB="1985-07-22")
    a3 = Author.objects.create(name="Mohammed Saleh", DOB="1990-03-15")

    b1 = Book.objects.create(
        title="Django Mastery",
        price=120,
        quantity=7,
        pubdate="2020-01-10",
        rating=4,
        publisher=p1
    )
    b1.authors.add(a1, a2)

    b2 = Book.objects.create(
        title="Python Deep Dive",
        price=90,
        quantity=3,
        pubdate="2018-06-15",
        rating=5,
        publisher=p2
    )
    b2.authors.add(a3)

    b3 = Book.objects.create(
        title="AI Revolution",
        price=200,
        quantity=1,
        pubdate="2016-09-20",
        rating=5,
        publisher=p3
    )
    b3.authors.add(a1)

    return HttpResponse("✔️ تمت تعبئة جميع البيانات بنجاح (لاب 8 + لاب 9)")


# ============================================================
#                     LAB 8 FUNCTIONS
# ============================================================

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'lab8/task1.html', {'books': books})


def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'lab8/task2.html', {'books': books})


def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) &
        ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'lab8/task3.html', {'books': books})


def lab8_task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'lab8/task4.html', {'books': books})


def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'lab8/task5.html', {'stats': stats})


def students_per_city(request):
    data = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'lab8/task7.html', {'data': data})


# ============================================================
#                     OLD FUNCTIONS
# ============================================================

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def list_all_books(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def index_old(request):
    name = request.GET.get("name", "world!")
    return HttpResponse(f"Hello, {name}")


def index2(request, val1):
    return HttpResponse(f"value1 = {val1}")


def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

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


# ============================================================
#                     TEMPLATE PAGES
# ============================================================

def index(request):
    return render(request, 'bookmodule/index.html')


def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def list_books(request):
    return render(request, 'bookmodule/list_books.html')


def view_one_book(request, book_id):
    return render(request, 'bookmodule/one_book.html', {"book_id": book_id})


def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='and')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
