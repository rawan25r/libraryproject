from django.db import models

# ============================================================
#                     TASK 3 (PRODUCT WITH IMAGE)
# ============================================================

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.name


# ============================================================
#                     TASK 2 (MANY-TO-MANY)
# ============================================================

class Address2(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.city} - {self.street}"


class Student2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name


# ============================================================
#                     TASK 1 (ONE-TO-ONE)
# ============================================================

class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city} - {self.street}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# ============================================================
#                     LAB 8 + LAB 9 (BOOK SYSTEM)
# ============================================================

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    # ============================
    #        LAB 9 FIELDS
    # ============================
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)

    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)

    # ============================
    #        LAB 8 FIELDS
    # ============================
    author = models.CharField(max_length=200, null=True)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title
