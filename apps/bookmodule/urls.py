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

    # PART 2 (Django Forms)
    path('lab9_part2/listbooks/', views.list_books_p2),
    path('lab9_part2/addbook/', views.add_book_p2),
    path('lab9_part2/editbook/<int:id>/', views.edit_book_p2),
    path('lab9_part2/deletebook/<int:id>/', views.delete_book_p2),
    
]
