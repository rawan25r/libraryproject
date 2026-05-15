from django.urls import path
from . import views

app_name = "bookmodule"

urlpatterns = [
    path('', views.index),

    # PART 1
    path('lab9_part1/listbooks/', views.list_books),
    path('lab9_part1/addbook/', views.add_book),
    path('lab9_part1/editbook/<int:id>/', views.edit_book),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book),

    # PART 2
    path('lab9_part2/listbooks/', views.list_books_p2),
    path('lab9_part2/addbook/', views.add_book_p2),
    path('lab9_part2/editbook/<int:id>/', views.edit_book_p2),
    path('lab9_part2/deletebook/<int:id>/', views.delete_book_p2),

    # TASK 1
    path("students/list/", views.list_students, name="list_students"),
    path("students/add/", views.add_student, name="add_student"),
    path("students/edit/<int:id>/", views.edit_student, name="edit_student"),
    path("students/delete/<int:id>/", views.delete_student, name="delete_student"),

    # TASK 2
    path("students2/list/", views.list_students2, name="list_students2"),
    path("students2/add/", views.add_student2, name="add_student2"),
    path("students2/edit/<int:id>/", views.edit_student2, name="edit_student2"),
    path("students2/delete/<int:id>/", views.delete_student2, name="delete_student2"),

    # TASK 3
    path("products/list/", views.list_products, name="list_products"),
    path("products/add/", views.add_product, name="add_product"),
    path("products/edit/<int:id>/", views.edit_product, name="edit_product"),
    path("products/delete/<int:id>/", views.delete_product, name="delete_product"),
]
