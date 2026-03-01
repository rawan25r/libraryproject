from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.aboutus, name='aboutus'),
    path('list/', views.list_books, name='list_books'),
    path('book/<int:book_id>/', views.view_one_book, name='view_one_book'),
]
