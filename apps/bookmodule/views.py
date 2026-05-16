from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Student, Address, Student2, Address2, Product
from .forms import BookForm, StudentForm, AddressForm, Student2Form, Address2Form, ProductForm

# ============================================================
#                     TASK 3 (IMAGE UPLOAD)
# ============================================================
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('/users/login')


@login_required(login_url='/users/login')
def listbooks(request):
    ...


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('/books/lab9_part1/listbooks')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'users/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        messages.success(request, "You have successfully registered")
        return redirect('/users/login')

    return render(request, 'users/register.html')

def list_products(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_products")
    else:
        form = ProductForm()
    return render(request, "products/add.html", {"form": form})

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("list_products")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/edit.html", {"form": form})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("list_products")

# ============================================================
#                     TASK 1 (ONE-TO-ONE)
# ============================================================

@login_required(login_url='/users/login')
def list_students(request):
    students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})

@login_required(login_url='/users/login')
def add_student(request):
    if request.method == "POST":
        aform = AddressForm(request.POST)
        sform = StudentForm(request.POST)
        if aform.is_valid() and sform.is_valid():
            address = aform.save()
            student = sform.save(commit=False)
            student.address = address
            student.save()
            return redirect("list_students")
    else:
        aform = AddressForm()
        sform = StudentForm()
    return render(request, "students/add.html", {"aform": aform, "sform": sform})

@login_required(login_url='/users/login')
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    address = student.address
    if request.method == "POST":
        aform = AddressForm(request.POST, instance=address)
        sform = StudentForm(request.POST, instance=student)
        if aform.is_valid() and sform.is_valid():
            aform.save()
            sform.save()
            return redirect("list_students")
    else:
        aform = AddressForm(instance=address)
        sform = StudentForm(instance=student)
    return render(request, "students/edit.html", {"aform": aform, "sform": sform})

@login_required(login_url='/users/login')
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.address.delete()
    student.delete()
    return redirect("list_students")

# ============================================================
#                     TASK 2 (MANY-TO-MANY)
# ============================================================

@login_required(login_url='/users/login')
def list_students2(request):
    students = Student2.objects.all()
    return render(request, "students2/list.html", {"students": students})

@login_required(login_url='/users/login')
def add_student2(request):
    if request.method == "POST":
        sform = Student2Form(request.POST)
        aform = Address2Form(request.POST)
        if sform.is_valid() and aform.is_valid():
            address = aform.save()
            student = sform.save(commit=False)
            student.save()
            student.addresses.add(address)
            return redirect("list_students2")
    else:
        sform = Student2Form()
        aform = Address2Form()
    return render(request, "students2/add.html", {"sform": sform, "aform": aform})

@login_required(login_url='/users/login')
def edit_student2(request, id):
    student = get_object_or__404(Student2, id=id)
    if request.method == "POST":
        sform = Student2Form(request.POST, instance=student)
        if sform.is_valid():
            sform.save()
            return redirect("list_students2")
    else:
        sform = Student2Form(instance=student)
    return render(request, "students2/edit.html", {"sform": sform})

@login_required(login_url='/users/login')
def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect("list_students2")

# ============================================================
#                     CRUD (LAB 10 PART 1 + PART 2)
# ============================================================

@login_required(login_url='/users/login')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/lab9_part1_list.html', {'books': books})

@login_required(login_url='/users/login')
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

@login_required(login_url='/users/login')
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

@login_required(login_url='/users/login')
def delete_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/books/lab9_part1/listbooks')

def index(request):
    return HttpResponse("Library Project Home Page")

# ============================================================
#                     LAB 10 PART 2 (Django Forms)
# ============================================================

@login_required(login_url='/users/login')
def list_books_p2(request):
    books = Book.objects.all()
    return render(request, 'books/lab9_part2_list.html', {'books': books})

@login_required(login_url='/users/login')
def add_book_p2(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')
    return render(request, 'books/lab9_part2_add.html', {'form': form})

@login_required(login_url='/users/login')
def edit_book_p2(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')
    return render(request, 'books/lab9_part2_edit.html', {'form': form})

@login_required(login_url='/users/login')
def delete_book_p2(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/books/lab9_part2/listbooks')
