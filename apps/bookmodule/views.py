from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Address, Student



def seed_all_data(request):

    # ============================
    # تعبئة جدول Address (المدن)
    # ============================
    riyadh = Address.objects.create(city="Riyadh")
    jeddah = Address.objects.create(city="Jeddah")
    dammam = Address.objects.create(city="Dammam")
    mecca = Address.objects.create(city="Mecca")
    medina = Address.objects.create(city="Medina")

    # ============================
    # تعبئة جدول Book (الكتب)
    # ============================
    Book.objects.create(title="Django for Beginners", author="Ali Ahmed", price=60, edition=1)
    Book.objects.create(title="Advanced Django", author="Sara Khalid", price=150, edition=4)
    Book.objects.create(title="Python Quick Guide", author="Mohammed Saleh", price=70, edition=2)
    Book.objects.create(title="Quality Software", author="Noura Hassan", price=95, edition=5)
    Book.objects.create(title="Data Structures", author="Fahad Omar", price=80, edition=3)
    Book.objects.create(title="Machine Learning", author="Aisha Abdullah", price=200, edition=6)
    Book.objects.create(title="SQL Mastery", author="Lama Youssef", price=55, edition=1)

    # ============================
    # تعبئة جدول Student (الطلاب)
    # ============================
    Student.objects.create(name="Aisha", age=20, address=riyadh)
    Student.objects.create(name="Fahad", age=22, address=jeddah)
    Student.objects.create(name="Lama", age=19, address=riyadh)
    Student.objects.create(name="Omar", age=23, address=dammam)
    Student.objects.create(name="Noura", age=21, address=mecca)
    Student.objects.create(name="Salem", age=24, address=medina)
    Student.objects.create(name="Reem", age=20, address=jeddah)

    return HttpResponse("✔️ تمت تعبئة جميع البيانات بنجاح")


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
#                     SIMPLE BOOK QUERIES
# ============================================================

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def list_all_books(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


# ============================================================
#                     OLD LAB FUNCTIONS
# ============================================================

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
#                     TEMPLATE PAGES (HTML/CSS)
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
