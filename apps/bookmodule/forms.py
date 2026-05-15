from django import forms
from .models import (
    Book,
    Student, Address,
    Student2, Address2,
    Product
)
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


# ============================================================
#                     TASK 3 (PRODUCT FORM)
# ============================================================

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


# ============================================================
#                     TASK 2 (MANY-TO-MANY)
# ============================================================



class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        exclude = ["addresses"]   # نخفي addresses من صفحة الإضافة


class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = "__all__"



# ============================================================
#                     TASK 1 (ONE-TO-ONE)
# ============================================================

class AddressForm(forms.ModelForm):
   class Meta:
       model = Address
       fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age"]  # حذف address من الفورم

# ============================================================
#                     LAB 9 (BOOK FORM)
# ============================================================

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating']
